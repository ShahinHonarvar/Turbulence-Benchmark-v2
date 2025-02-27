from itertools import islice, cycle

def lists_with_product_equal_n(lst):

    def sublists_with_product_equal_n(lst, n):
        result = []
        for i in range(1, len(lst) + 1):
            for j in range(len(lst) - i + 1):
                if (sublst := lst[j:j + i]):
                    if sublst[0] == 0 and len(sublst) > 1:
                        continue
                    if sublst[0] < 0 and len(sublst) % 2 == 0:
                        continue
                    if sublst[0] > 0 and len(sublst) % 2 == 1:
                        continue
                    if sublst[0] == 0 and len(sublst) == 1:
                        continue
                    if sublst[0] == -n and all((x > 0 for x in sublst[1:])):
                        result.append(sublst)
                        continue
                    if sublst[0] * n > 0 and all((x > 0 for x in sublst)):
                        continue
                    if sublst[0] * n < 0 and all((x < 0 for x in sublst)):
                        continue
                    if sublst[0] * n < 0 and all((x > 0 for x in sublst)):
                        continue
                    if sublst[0] * n > 0 and all((x < 0 for x in sublst)):
                        continue
                    if sublst[0] * n == 0:
                        continue
                    if (prod := (sublst[0] * n)):
                        if sublst[1:] == [prod // sublst[0]]:
                            result.append(sublst)
        return result
    return [sublist for sublist in sublists_with_product_equal_n(lst, -20) if sublist]