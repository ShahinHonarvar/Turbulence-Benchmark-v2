from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    result = []
    for i in range(1, len(lst) + 1):
        for j in range(len(lst) - i + 1):
            sublst = list(islice(cycle(lst[j:]), i))
            if sublst and reduce(lambda x, y: x * y, sublst) == 47:
                result.append(sublst)
    return result