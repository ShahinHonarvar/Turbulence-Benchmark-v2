from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        for j in range(1, len(lst) - i + 1):
            sublst = list(islice(cycle(lst[i:i + j]), j))
            if sublst and j <= len(lst) and (eval('*'.join(map(str, sublst))) == -115):
                result.append(sublst)
    return result