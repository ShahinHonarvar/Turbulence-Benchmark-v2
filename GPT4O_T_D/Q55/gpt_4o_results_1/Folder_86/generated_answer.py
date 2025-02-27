def lists_with_product_equal_n(circular_list):
    target_product = -779
    result = []
    n = len(circular_list)
    for i in range(n):
        product = 1
        for j in range(n):
            product *= circular_list[(i + j) % n]
            if product == target_product:
                start = i
                end = (i + j) % n
                if end >= start:
                    result.append(circular_list[start:end + 1])
                else:
                    result.append(circular_list[start:] + circular_list[:end + 1])
            if j == n - 1:
                break
    return result