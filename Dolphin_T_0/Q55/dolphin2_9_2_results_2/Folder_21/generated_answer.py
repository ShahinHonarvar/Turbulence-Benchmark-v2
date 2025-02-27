def list_with_product_equal_n(lst):
    n = len(lst)
    lst = lst + lst[:2]
    result = []
    for start in range(n + 2):
        product = 1
        for end in range(start, n + start + 1):
            product *= lst[end]
            if product > 851:
                break
            if product == 851:
                t = []
                for i in range(start, end + 1):
                    t.append(lst[i % n])
                result.append(t)
    return result