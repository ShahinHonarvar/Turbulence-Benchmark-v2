from itertools import islice, cycle

def lists_with_product_equal_n(lst, n=83):
    result = []
    for i in range(len(lst)):
        sublst = [lst[i]]
        for j in range(i + 1, len(lst)):
            sublst.append(lst[j])
            if sublst[-1] == 0:
                break
            if sublst[-1] < 0 and sublst.count(sublst[-1]) > 1:
                break
            if sublst[-1] < 0 and sublst.count(sublst[-1]) % 2 == 1:
                sublst = sublst[:-1]
            if sublst[-1] < 0 and sublst.count(sublst[-1]) % 2 == 0:
                sublst = sublst[:-2]
            if sublst[-1] > 0 and sublst.count(sublst[-1]) > 1:
                sublst = sublst[:-1]
            if sublst[-1] > 0 and sublst.count(sublst[-1]) % 2 == 1:
                sublst = sublst[:-2]
            if sublst[-1] > 0 and sublst.count(sublst[-1]) % 2 == 0:
                sublst = sublst[:-1]
            if sublst[-1] == 0:
                break
            if sublst[-1] > 0 and sublst[-1] * sublst[:-1] == n:
                result.append(sublst)
                break
    return result