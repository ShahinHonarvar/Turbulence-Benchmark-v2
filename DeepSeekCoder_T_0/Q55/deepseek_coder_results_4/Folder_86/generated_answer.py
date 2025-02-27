def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    target = -779
    result = []
    for start in range(n):
        product = 1
        sublist = []
        for i in range(n):
            idx = (start + i) % n
            product *= circular_list[idx]
            sublist.append(circular_list[idx])
            if product == target:
                result.append(sublist.copy())
            if product == 0 or product > target:
                break
        if product == target:
            break
    return result