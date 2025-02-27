from itertools import islice, cycle

def lists_with_product_equal_n(lst):

    def sublists_with_product_equal_n(lst, n):
        for i in range(1, len(lst) + 1):
            for j in range(len(lst) - i + 1):
                if lst[j] * sublists_with_product_equal_n(lst[j + 1:j + i], n) == n:
                    return [lst[j:j + i]]
        return []
    return [sublist for sublist in [sublists_with_product_equal_n(lst[i:] + lst[:i], 99) for i in range(1, len(lst) + 1)] if sublist]