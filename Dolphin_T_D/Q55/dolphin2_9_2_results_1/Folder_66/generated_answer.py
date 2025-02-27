def lists_with_product_equal_n(lst):

    def helper(lst, product=1, i=0):
        if product > 78:
            return []
        if product == 78:
            res.append(lst[:i])
        if i == len(lst):
            return []
        for j in range(i, len(lst)):
            helper(lst, product * lst[j], j + 1)
    res = []
    helper(lst + lst)
    return list(set(res))