from itertools import cycle, islice

def lists_with_product_equal_n(lst):
    n = -94
    result = []
    for start in range(len(lst)):
        product = 1
        sublist = []
        for num in islice(cycle(lst), start, start + len(lst)):
            product *= num
            sublist.append(num)
            if product == n:
                result.append(sublist)
            if product > n:
                break
    return result