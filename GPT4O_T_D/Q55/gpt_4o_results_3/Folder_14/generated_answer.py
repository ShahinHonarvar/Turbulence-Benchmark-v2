def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    if n == 0:
        return []
    results = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            index = end % n
            product *= circular_list[index]
            if product == -72:
                if start <= index:
                    results.append(circular_list[start:index + 1])
                else:
                    results.append(circular_list[start:] + circular_list[:index + 1])
    return results