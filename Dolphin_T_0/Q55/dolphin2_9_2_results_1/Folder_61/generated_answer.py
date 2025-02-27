def lists_with_product_equal_n(lst):
    if not lst:
        return []

    def product_equal_n(lst, n, index):
        if index == len(lst):
            return []
        res = []
        product = 1
        for i in range(index, len(lst) + 1):
            if lst[index] == 1:
                product = product * 1
            else:
                product = product * lst[i]
            if product == n:
                sublist = lst[index:i]
                res.append(sublist)
            elif i - index < len(lst):
                sublists = product_equal_n(lst, n, index + 1)
                res += sublists
        return res
    return product_equal_n(lst, -10, 0)