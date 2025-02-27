from itertools import islice, cycle

def lists_with_product_equal_n(lst):

    def sublists_with_product(lst, target, acc, product_so_far):
        if product_so_far == target and len(lst) >= len(acc):
            return [list(acc)]
        res = []
        for i in range(len(lst)):
            new_lst = lst[i + 1:] + lst[:i + 1]
            new_acc = acc + new_lst[:1]
            new_product = product_so_far * new_lst[0]
            res.extend(sublists_with_product(new_lst[1:], target, new_acc, new_product))
        return res
    clst = list(lst)
    clst.extend(lst[:1])
    return sublists_with_product(clst, -87, [lst[0]], lst[0])