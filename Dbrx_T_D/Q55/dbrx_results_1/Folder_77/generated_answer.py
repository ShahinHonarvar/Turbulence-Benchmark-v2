from itertools import islice

def lists_with_product_equal_n(lst):
    sublists = []
    for i in range(len(lst)):
        sublst = []
        product = 1
        for j in range(i, len(lst)):
            sublst.append(lst[j])
            product *= lst[j]
            if product == 632:
                sublists.append(sublst.copy())
                break
            elif product > 632:
                break
        for j in range(i + 1, len(lst)):
            sublst.pop()
            product //= lst[j - 1]
            if product == 632:
                sublists.append(sublst.copy())
                break
            elif product < 632:
                break
    return sublists