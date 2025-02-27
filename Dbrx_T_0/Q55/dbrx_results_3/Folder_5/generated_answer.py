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
                    if sublst[0] == n and all((x < 0 for x in sublst[1:])):
                        result.append(sublst)
                        continue
                    if sublst[0] * n < 0 and all((x * n > 0 for x in sublst[1:])):
                        result.append(sublst)
                        continue
                    if sublst[0] * n > 0 and all((x * n < 0 for x in sublst[1:])):
                        result.append(sublst)
                        continue
        return result
    return [sublst for sublst in sublists_with_product_equal_n(lst, -33) if sublst[0] != 0 and all((x != 0 for x in sublst[1:]))]