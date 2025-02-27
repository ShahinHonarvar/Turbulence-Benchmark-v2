from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    n = 83
    result = []
    for i in range(len(lst)):
        for j in range(1, len(lst) - i + 1):
            if list(islice(cycle(lst), i, i + j)) == list(islice(cycle(lst[i:i + j]), i, i + j)):
                if n in (k := [x for x in product(lst[i:i + j], repeat=1)])[1:] or j == 1:
                    result.append(lst[i:i + j])
    return result