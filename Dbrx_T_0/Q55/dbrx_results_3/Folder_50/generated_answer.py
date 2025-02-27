from itertools import islice, cycle

def lists_with_product_equal_n(lst):

    def sublists_with_product_equal_n(lst, n):
        result = []
        for i in range(1, len(lst) + 1):
            for j in range(len(lst) - i + 1):
                if (sublst := [x for x in islice(cycle(lst), j, j + i) if x != 0]):
                    if sublst[0] == 0:
                        sublst = sublst[1:]
                    if (prod := all((x * y != 0 for x, y in zip(sublst, sublst[1:])))):
                        if (prod := (prod and reduce(lambda x, y: x * y, sublst) == n)):
                            result.append(sublst)
        return result
    return sublists_with_product_equal_n(lst, 45)