def lists_with_product_equal_n(circular_list):
    n = -10
    res = []
    for i in range(len(circular_list)):
        p = 1
        for j in range(i, len(circular_list)):
            p *= circular_list[j % len(circular_list)]
            if p == n:
                res.append(circular_list[i:j + 1])
    return res