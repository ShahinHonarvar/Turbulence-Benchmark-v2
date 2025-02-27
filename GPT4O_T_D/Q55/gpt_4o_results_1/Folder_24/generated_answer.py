def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(1, n + 1):
            product = 1
            sublist = []
            for i in range(end):
                index = (start + i) % n
                sublist.append(circular_list[index])
                product *= circular_list[index]
                if product == -89:
                    result.append(sublist.copy())
                    break
                elif abs(product) > abs(-89):
                    break
    return result