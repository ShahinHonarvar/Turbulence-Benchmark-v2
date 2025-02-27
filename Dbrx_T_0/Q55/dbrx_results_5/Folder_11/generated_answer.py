from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        window = list(islice(cycle(lst[i:]), len(lst)))
        for j in range(1, len(window) + 1):
            sublst = window[:j]
            if sublst[0] == 0 and len(sublst) > 1:
                continue
            if sublst[0] == 1:
                break
            if sublst[0] == -1 and len(sublst) % 2 == 0:
                break
            if sublst[0] == -1 and len(sublst) % 2 == 1:
                sublst = sublst[1:]
            if sublst[0] == -15:
                result.append(sublst)
                break
            if sublst[0] * -1 in sublst[1:]:
                result.append(sublst)
                break
            if sublst[0] * -1 == sublst[-1]:
                result.append(sublst)
                break
    return result