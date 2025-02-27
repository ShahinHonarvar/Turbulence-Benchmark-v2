def lists_with_product_equal_n(lst):

    def find_sublists(l, n, product, sublist):
        if len(l) == 0 or product == 1:
            return
        elif product == n:
            res.append(sublist)
            find_sublists(l, n, product, sublist[:-1])
        else:
            find_sublists(l[1:], n, product * l[0], sublist + [l[0]])
            find_sublists(l[1:], n, product, sublist)
    res = []
    find_sublists(lst, -3, 1, [])
    return res