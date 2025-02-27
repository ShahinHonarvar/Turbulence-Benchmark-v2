def lists_with_product_equal_n(lst):
    lst *= 2
    n = -779
    res = []
    for i in range(len(lst)):
        p = 1
        for j in range(i, len(lst)):
            p *= lst[j]
            if p == n:
                res.append(lst[i:j + 1])
            if p > n:
                break
    return [sublist for sublist in res if len(sublist) <= len(lst) // 2]