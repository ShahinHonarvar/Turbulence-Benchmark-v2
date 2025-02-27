from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):

    def sublists_with_product_equal_n(sublist):
        for i in range(1, len(sublist) + 1):
            for j in range(len(sublist) - i + 1):
                if sublist[j:j + i] not in sublists and prod(sublist[j:j + i]) == 46:
                    sublists.append(sublist[j:j + i])
                    yield sublist[j:j + i]
                    sublists.remove(sublist[j:j + i])

    def prod(iterable):
        result = 1
        for i in iterable:
            result *= i
        return result
    sublists = []
    circular_list = list(circular_list)
    circular_sublists = [list(islice(circular_list, i)) for i in range(len(circular_list) + 1)]
    for circular_sublist in circular_sublists:
        sublists_with_product_equal_n(circular_sublist)
    return list({tuple(sublist) for sublist in sublists})