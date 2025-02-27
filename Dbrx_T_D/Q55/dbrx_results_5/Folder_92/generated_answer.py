from itertools import islice, cycle

def sublists_with_product_equal_n(lst, n=5):
    circular_lst = cycle(lst)
    sublists = []
    prod = 1
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublist = list(islice(circular_lst, j - i + 1))
            prod = prod * sublist[0]
            sublist.append(prod)
            if prod == n:
                sublists.append(sublist[:sublist.index(prod)])
            prod = 1
    return sublists