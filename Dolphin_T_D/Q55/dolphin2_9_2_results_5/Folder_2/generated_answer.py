def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            v = 1
            for k in range(i, j + i + 1):
                v *= lst[k % n]
            if v == -968:
                m = j - i + 1
                is_in = False
                for m_ in result:
                    if len(m_) == m and m_ in [lst[k % n] for k in range(i, j + i + 1)]:
                        is_in = True
                        break
                if not is_in:
                    result.append([lst[k % n] for k in range(i, j + i + 1)])
    return result