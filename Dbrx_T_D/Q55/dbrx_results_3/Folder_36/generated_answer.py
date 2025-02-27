from itertools import combinations

def lists_with_product_equal_n(circular_list):

    def prod(lst):
        return reduce(lambda x, y: x * y, lst)

    def circular_sublists(lst, n):
        return [lst[i:j] for i in range(len(lst)) for j in range(i + n, len(lst) + n) if j - i == n]
    return [sl for sl in sublists if prod(sl) == 714]

def sublists(lst):
    return [lst[i:j] for i in range(len(lst)) for j in range(i + 1, len(lst) + 1)]