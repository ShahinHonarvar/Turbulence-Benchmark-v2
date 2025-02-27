def lists_with_product_equal_n(circular_list):
    n = 851
    result = []
    size = len(circular_list)
    for start in range(size):
        product = 1
        for end in range(size):
            idx = (start + end) % size
            product *= circular_list[idx]
            if product == n:
                if start <= idx:
                    result.append(circular_list[start:idx + 1])
                else:
                    result.append(circular_list[start:] + circular_list[:idx + 1])
            elif product == 0 or product > n:
                break
    return result