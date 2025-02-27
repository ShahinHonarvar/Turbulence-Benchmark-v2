def lists_with_product_equal_n(ls):

    def helper(i, prod):
        if prod == n and i != 0:
            lists.append(lst[:i])
        if i == len(ls):
            return
        for j in range(i, len(ls)):
            lst.append(ls[j])
            helper(j + 1, prod * lst[-1])
            lst.pop()
    n = -81
    lists = []
    lst = []
    for i in range(len(ls)):
        helper(i, 1)
    return lists