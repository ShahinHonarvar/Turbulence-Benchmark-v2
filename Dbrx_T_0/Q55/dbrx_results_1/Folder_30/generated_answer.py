from itertools import islice, cycle

def lists_with_product_equal_n(lst):

    def sublists_with_product_equal_n(lst, n):
        for i in range(1, len(lst) + 1):
            for j in range(len(lst) - i + 1):
                sublist = lst[j:j + i]
                if n == 1 and len(sublist) == 1 and (sublist[0] == 1):
                    yield [sublist]
                elif n == sublist[0] and all((x == 1 for x in sublist[1:])):
                    yield [sublist]
                elif n % sublist[0] == 0:
                    for result in sublists_with_product_equal_n(sublist[1:], n // sublist[0]):
                        yield ([sublist[0]] + result)
    return list(set((tuple(sorted(sublist)) for sublist in sublists_with_product_equal_n(lst, 99))))

def circular_list(lst):
    return list(islice(cycle(lst), len(lst)))