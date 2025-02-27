def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            idx = end % n
            product *= circular_list[idx]
            if product == 93:
                if start <= idx:
                    result.append(circular_list[start:idx + 1])
                else:
                    result.append(circular_list[start:] + circular_list[:idx + 1])
            elif product == 0 or product > 93:
                break
    return result