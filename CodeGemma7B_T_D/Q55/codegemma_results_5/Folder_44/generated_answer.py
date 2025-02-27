from itertools import product

def lists_with_product_equal_n(clist):
    result = []
    for i in range(len(clist) - 3):
        for sublist in product(*(clist[i:i + 4], clist)):
            if len(set(sublist)) == 4 and reduce(lambda x, y: x * y, sublist) == 29:
                result.append(sorted(list(set(sublist))))
    return result