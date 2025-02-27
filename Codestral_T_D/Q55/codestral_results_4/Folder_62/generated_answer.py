from collections import deque

def lists_with_product_equal_n(lst):

    def product(lst):
        prod = 1
        for num in lst:
            prod *= num
        return prod

    def calc_sublists(lst):
        lst = deque(lst)
        sublists = []
        for _ in range(len(lst)):
            for i in range(1, len(lst) + 1):
                sublist = list(lst)[:i]
                if product(sublist) == 100:
                    sublists.append(sublist)
            lst.rotate(-1)
        return sublists
    return calc_sublists(lst)