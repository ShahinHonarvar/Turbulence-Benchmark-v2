def lists_with_product_equal_n(lst):

    def get_sublists(lst, n):
        res = []
        for i in range(len(lst)):
            if lst[i] == 2:
                prev = i - 1
                cur = i
                while cur < len(lst):
                    if lst[cur] != 0:
                        if prev == -1 or lst[prev] * lst[cur] == n:
                            res.append(lst[i:cur + 1])
                        prev = cur
                    cur += 1
        return res

    def is_circular_list_equal(lst1, lst2):
        s1 = set(lst1)
        s2 = set(lst2)
        return s1 == s2

    def circular_shift(lst, n):
        return lst[n:] + lst[:n]
    res = []
    for i in range(len(lst)):
        if lst[i] != 2:
            continue
        if i + 1 == len(lst):
            lst_cycle = circular_shift(lst, 0)
        else:
            lst_cycle = circular_shift(lst, i + 1)
        sublists = get_sublists(lst_cycle, 2)
        for sublist in sublists:
            if is_circular_list_equal(sublist, lst):
                res.append(sublist)
    return res