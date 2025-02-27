from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    result = []
    n = -93

    def product(sublist):
        prod = 1
        for num in sublist:
            prod *= num
        return prod
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublist = list(islice(cycle(lst[i:j + 1]), len(lst)))
            if product(sublist) == n:
                result.append(sublist)
    return result