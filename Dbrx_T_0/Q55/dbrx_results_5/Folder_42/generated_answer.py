from itertools import islice, cycle

def lists_with_product_equal_n(lst, n=25):

    def sublists_with_product(lst, n):
        for i in range(1, len(lst) + 1):
            for j in range(len(lst) - i + 1):
                sublist = lst[j:j + i]
                if n == 1:
                    yield sublist
                elif n % sublist[0] == 0:
                    yield from sublists_with_product(sublist[1:], n // sublist[0])
    circular_lst = list(islice(cycle(lst), len(lst) * 2))
    return list(set(sublists_with_product(circular_lst, n)))