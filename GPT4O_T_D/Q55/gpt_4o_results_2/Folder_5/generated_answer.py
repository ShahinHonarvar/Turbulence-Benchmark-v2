def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for end in range(n):
            idx = (start + end) % n
            product *= circular_list[idx]
            if product == -33:
                if start <= idx:
                    result.append(circular_list[start:idx + 1])
                else:
                    result.append(circular_list[start:] + circular_list[:idx + 1])
            if end == n - 1:
                break
    return result