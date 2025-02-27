def lists_with_product_equal_n(circular_list):
    n = -779
    result = []
    list_size = len(circular_list)
    for start in range(list_size):
        product = 1
        for end in range(start, list_size + start):
            end_index = end % list_size
            product *= circular_list[end_index]
            if product == n:
                result.append(circular_list[start:end_index + 1])
            elif product > abs(n):
                break
    return result