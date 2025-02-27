def lists_with_product_equal_n(lst):

    def product(lst):
        p = 1
        for i in lst:
            p *= i
        return p

    def find_sublists(lst, n, start=0, end=None):
        if end is None:
            end = len(lst)
        if start == end:
            return []
        lst = lst[start:end]
        if product(lst) == n:
            return [lst]
        ret = []
        for i in range(len(lst)):
            ret.extend(find_sublists(lst, n, i, end))
        return ret
    return find_sublists(lst + lst, 96)