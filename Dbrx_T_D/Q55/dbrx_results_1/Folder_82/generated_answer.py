from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        sublst = []
        product = 1
        for j in range(i, i + len(lst)):
            element = lst[j % len(lst)]
            sublst.append(element)
            product *= element
            if product == 8:
                result.append(sublst)
            elif product > 8:
                break
    return result