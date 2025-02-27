def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []
    for start in range(n):
        product = 1
        for end in range(n):
            index = (start + end) % n
            product *= circular_list[index]
            if product == -22:
                if start <= index:
                    results.append(circular_list[start:index + 1])
                else:
                    results.append(circular_list[start:] + circular_list[:index + 1])
            if abs(product) > abs(-22):
                break
    return results