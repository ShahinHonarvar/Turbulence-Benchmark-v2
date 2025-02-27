def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for size in range(1, n + 1):
        for start_idx in range(n):
            product = 1
            sublist = []
            for idx in range(start_idx, start_idx + size):
                if idx == n:
                    idx = 0
                sublist.append(lst[idx])
                product *= lst[idx]
            if product == -22:
                result.append(sublist)
    return result