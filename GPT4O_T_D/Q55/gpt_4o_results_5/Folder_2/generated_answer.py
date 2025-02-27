def lists_with_product_equal_n(circular_list):
    target_product = -968
    n = len(circular_list)
    results = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            index = end % n
            product *= circular_list[index]
            if product == target_product:
                if start <= index:
                    results.append(circular_list[start:index + 1])
                else:
                    results.append(circular_list[start:] + circular_list[:index + 1])
            if product == 0:
                break
    return results