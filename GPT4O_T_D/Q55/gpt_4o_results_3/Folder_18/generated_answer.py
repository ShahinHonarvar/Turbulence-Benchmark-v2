def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            end = (start + length - 1) % n
            product *= circular_list[end]
            if product == 36:
                if start <= end:
                    result.append(circular_list[start:end + 1])
                else:
                    result.append(circular_list[start:] + circular_list[:end + 1])
            if product == 0:
                break
            if length == n:
                break
    return result