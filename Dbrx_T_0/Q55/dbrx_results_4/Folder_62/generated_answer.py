from itertools import islice, cycle

def lists_with_product_equal_n(lst):

    def sublists_with_product_equal_n(lst, n):
        result = []
        for i in range(1, len(lst) + 1):
            for j in range(len(lst) - i + 1):
                if (sublst := [x for x in islice(cycle(lst), j, j + i) if x != 0 and x != 1]):
                    if sublst[0] == 0:
                        continue
                    if sublst[0] == 1:
                        sublst = sublst[1:]
                    if sublst and all((x == 1 for x in sublst)):
                        continue
                    if (prod := sublst[0]):
                        for x in sublst[1:]:
                            prod *= x
                        if prod == n:
                            result.append(sublst)
        return result
    return sublists_with_product_equal_n(lst, 100)