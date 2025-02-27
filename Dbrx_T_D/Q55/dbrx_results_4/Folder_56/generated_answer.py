from itertools import islice, cycle, product

def lists_with_product_equal_n(lst, n):
    result = []
    for i in range(1, len(lst) + 1):
        for j in product(cycle(lst), repeat=i):
            if len(j) == 1:
                continue
            if sum((x for x in j)) == n and sum((x * y for x, y in zip(j, islice(j, 1, i)))) == 0:
                result.append(list(j))
    return result