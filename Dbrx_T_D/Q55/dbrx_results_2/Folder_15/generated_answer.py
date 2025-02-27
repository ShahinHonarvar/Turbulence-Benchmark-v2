from itertools import islice, cycle

def lists_with_product_equal_n(lst):

    def sublists(lst):
        n = len(lst)
        for i in range(n):
            for j in range(i, n):
                yield lst[i:j + 1]

    def product(lst):
        p = 1
        for i in lst:
            p *= i
        return p
    result = []
    for sublist in sublists(lst):
        if product(sublist) == -7:
            result.append(sublist)
    return result