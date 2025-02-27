def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            index = (start + length - 1) % n
            product *= circular_list[index]
            if product == -690:
                slice_start = start
                slice_end = start + length
                if slice_end <= n:
                    result.append(circular_list[slice_start:slice_end])
                else:
                    result.append(circular_list[slice_start:] + circular_list[:slice_end % n])
    return result