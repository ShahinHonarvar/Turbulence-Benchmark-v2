from itertools import islice, cycle, combinations

def lists_with_product_equal_n(lst):
    n = len(lst)
    res = set()

    def helper(it1, it2):
        for x in it1:
            for y in it2:
                if x[0] == 1 and y[0] == 1:
                    if x[1]:
                        res.add(x[1])
                    if y[1]:
                        res.add(y[1])
                else:
                    imul = x[0] * y[0]
                    helper(islice(cycle(lst), x[2] - 1, None, n), islice(cycle(lst), y[2] - 1, None, n))
    lstc = cycle(lst)
    for x in combinations(range(n), 2):
        helper(islice(lstc, x[0] - 1, None, n), islice(lstc, x[1] - 1, None, n))
    return list(map(list, sorted(res, key=len)))