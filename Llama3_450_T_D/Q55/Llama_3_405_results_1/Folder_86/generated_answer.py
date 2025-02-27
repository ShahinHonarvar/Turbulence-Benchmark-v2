def lists_with_product_equal_n(lst):
    n = len(lst)
    target_product = -779
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= lst[(i + j) % n]
            if product == target_product:
                result.append([lst[(i + k) % n] for k in range(j + 1)])
    return result