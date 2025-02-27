from itertools import islice, cycle

def lists_with_product_equal_n(lst):

    def sublists_with_product_equal_n(lst, n):
        result = []
        for i in range(1, len(lst) + 1):
            for j in range(len(lst) - i + 1):
                sublist = lst[j:j + i]
                if reduce(lambda x, y: x * y, sublist, 1) == n:
                    result.append(sublist)
        return result
    circular_lst = list(islice(cycle(lst), len(lst) * 2))
    return sublists_with_product_equal_n(circular_lst, 47)