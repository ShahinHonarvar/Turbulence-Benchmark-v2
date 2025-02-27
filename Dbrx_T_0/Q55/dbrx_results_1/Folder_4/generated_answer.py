from itertools import islice, cycle

def lists_with_product_equal_n(lst):

    def sublists_with_product_equal_n(lst, n):
        for i in range(1, len(lst) + 1):
            for j in range(len(lst) - i + 1):
                sublist = lst[j:j + i]
                if n == 1 and (not sublist):
                    yield []
                elif n == 1 and sublist == [1]:
                    yield sublist
                elif sublist and all((x > 0 for x in sublist)) and (n == reduce(lambda x, y: x * y, sublist)):
                    yield sublist
    return list(set(sublists_with_product_equal_n(lst, 91) | sublists_with_product_equal_n(cycle(lst), 91)))