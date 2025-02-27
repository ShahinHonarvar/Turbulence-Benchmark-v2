from itertools import islice, cycle

def lists_with_product_equal_n(numbers):
    result = []
    for i in range(len(numbers)):
        window = islice(cycle(numbers), i, i + len(numbers))
        sublist = [x for x in zip(*[window] * n)]
        if any((x == 27 for x in (prod(sublist[i]) for i in range(len(sublist))))):
            result.append(sublist)
    return result