def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    circular_list += circular_list
    result = []
    for i in range(n):
        for j in range(i, i + n):
            product = 1
            for k in range(i, j + 1):
                product *= circular_list[k]
                if product > 36:
                    break
                elif product == 36:
                    result.append(circular_list[i:j + 1])
    return result