from itertools import permutations

def lists_with_product_equal_n(lst):
    size = len(lst)
    lst += lst[:size - 1]
    product_sublists = []
    for i in range(size):
        for j in range(i + 1, i + size):
            product = 1
            sublist = []
            for k in range(i, j + 1):
                product *= lst[k]
                sublist.append(lst[k])
                if product == 10:
                    product_sublists.append(sublist)
                elif product > 10:
                    break
    return product_sublists