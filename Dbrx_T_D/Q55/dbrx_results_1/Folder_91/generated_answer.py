from itertools import islice, cycle

def circular_slice(lst, start, end):
    n = len(lst)
    return islice(cycle(lst), start, end, n)

def lists_with_product_equal_n(lst, target=2):
    result = []
    for i in range(len(lst)):
        sublst = []
        product = 1
        while product != target:
            sublst.append(lst[i])
            product *= lst[i]
            i = (i + 1) % len(lst)
            if len(sublst) > len(lst):
                break
        if product == target:
            result.append(sublst)
    return result