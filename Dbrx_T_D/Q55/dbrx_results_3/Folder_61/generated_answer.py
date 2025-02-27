from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        sublist = []
        for j in range(i, len(lst)):
            if product * lst[j] == -10:
                result.append(sublist)
                break
            elif product * lst[j] < -10:
                break
            else:
                product *= lst[j]
                sublist.append(lst[j])
    return result