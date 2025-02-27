from itertools import cycle

def lists_with_product_equal_n(lst):
    c = cycle(lst)
    for i in range(len(lst)):
        product = 1
        sublst = []
        for j in range(i, len(lst)):
            element = next(c)
            product *= element
            sublst.append(element)
            if product == 29:
                yield sublst
            elif product > 29:
                break