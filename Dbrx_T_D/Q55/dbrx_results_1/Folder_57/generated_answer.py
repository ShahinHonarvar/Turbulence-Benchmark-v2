from itertools import islice, cycle

def lists_with_product_equal_n(lst, target):
    prod = 1
    result = []
    i = 0
    while i < len(lst):
        if lst[i] != 0:
            prod *= lst[i]
            sublst = [lst[i]]
            for j in range(i + 1, len(lst)):
                if lst[j] != 0:
                    prod *= lst[j]
                    sublst.append(lst[j])
                else:
                    prod //= lst[j]
                if prod == target:
                    result.append(sublst)
        prod //= lst[i]
        i += 1
    for sublst in result:
        if len(sublst) > len(lst):
            result.remove(sublst)
    return result