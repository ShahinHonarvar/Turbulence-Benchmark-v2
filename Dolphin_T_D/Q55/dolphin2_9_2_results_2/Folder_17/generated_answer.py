def lists_with_product_equal_n(lst):
    if len(lst) < 1:
        return []
    else:
        lst = lst + lst[:1]
        n = 18
        result = []
        i, j = (0, 0)
        product = 1
        while j < len(lst):
            while product < n and j < len(lst):
                product *= lst[j]
                j += 1
            if product == n:
                result.append(lst[i:j])
            if j < len(lst):
                product = product // lst[i]
                i += 1
        return result