from itertools import islice, cycle, combinations

def lists_with_product_equal_n(lst):

    def circular_slice(circular_lst, start, end):
        return islice(circular_lst, start, end) if start < end else islice(circular_lst, start, None) + islice(circular_lst, 0, end)
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublst = list(circular_slice(lst, i, j))
            if len(sublst) > 0 and all((elt >= 0 for elt in sublst)) and all((elt != 1 for elt in sublst)) and all((elt not in (-1, 1, 2, 3, 9) for elt in sublst)) and (not all((elt == 3 for elt in sublst))) and (not all((elt == 27 for elt in sublst))):
                if max(sublst) > 10 or product(sublst) == 27:
                    result.append(sublst)
    return result

def product(lst):
    res = 1
    for elt in lst:
        res *= elt
        if res > 27:
            break
    return res