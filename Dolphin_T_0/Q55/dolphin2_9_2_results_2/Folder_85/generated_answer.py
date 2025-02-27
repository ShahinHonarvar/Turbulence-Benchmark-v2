from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    n = -97
    size = len(lst)
    lst = list(cycle(lst))
    ans = []
    for i in range(size * 2 - 1):
        sublist = []
        product = 1
        for j in range(i, i + size):
            if product != n:
                product *= lst[j % size]
                if j + 1 < i + size:
                    product *= lst[(j + 1) % size]
                    sublist.append(lst[j % size])
                elif product == n and j + 1 == i + size:
                    sublist.append(lst[j % size])
            else:
                ans.append(sublist)
                break
    return ans