from itertools import islice, cycle, combinations

def lists_with_product_equal_n(lst, n=32):

    def circular_sublists(lst):
        circular_lst = lst + lst[:1]
        return (circular_lst[i:i + size] for i in range(len(lst)) for size in range(1, len(lst) + 1))

    def product_circular_sublist(lst):
        return reduce(lambda x, y: x * y, lst, 1)
    result = []
    for sub_lst in circular_sublists(lst):
        if product_circular_sublist(sub_lst) == n:
            result.append(sub_lst)
    return result