from itertools import islice, cycle

def lists_with_product_equal_n(lst, n=40):

    def sublists_with_product(lst, n):
        for i in range(1, len(lst) + 1):
            for j in range(len(lst) - i + 1):
                sublist = lst[j:j + i]
                if n == 1:
                    yield sublist
                elif n > 1 and all((num != 0 for num in sublist)):
                    product = 1
                    for num in sublist:
                        product *= num
                    if product == n:
                        yield sublist
    return list(set(sublists_with_product(lst, n))) if any(sublists_with_product(lst, n)) else []

def circular_sublists(lst, n):
    return [list(islice(cycle(lst), i, i + len(lst))) for i in range(n)]

def circular_lists_with_product_equal_n(lst, n=40):
    return lists_with_product_equal_n(circular_sublists(lst, len(lst)), n)