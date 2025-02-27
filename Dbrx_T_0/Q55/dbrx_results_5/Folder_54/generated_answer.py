from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        sublst = [lst[i]]
        product = lst[i]
        for j in range(i + 1, len(lst)):
            sublst.append(lst[j])
            product *= lst[j]
            if product == -17:
                result.append(sublst.copy())
            elif product > -17:
                break
    return result