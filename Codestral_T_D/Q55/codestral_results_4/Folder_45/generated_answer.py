from itertools import cycle, islice

def lists_with_product_equal_n(lst):
    n = -5
    result = []
    for i in range(len(lst)):
        product = 1
        sublist = []
        for j in islice(cycle(lst), i, i + len(lst)):
            product *= j
            sublist.append(j)
            if product == n:
                result.append(sublist)
            elif product > n:
                break
    return result