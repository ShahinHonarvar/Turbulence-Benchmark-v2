from itertools import combinations, islice

def lists_with_product_equal_n(circular_list):

    def sublists_with_product_equal_n(lst, n):
        for i in range(1, len(lst) + 1):
            for j in combinations(lst, i):
                if sublists_product(j) == n:
                    yield list(j)

    def circular_sublists_with_product_equal_n(lst, n):
        for i in range(1, len(lst) + 1):
            for j in combinations(range(len(lst) + i - 1), i):
                sublst = [lst[k % len(lst)] for k in j]
                if sublists_product(sublst) == n:
                    yield sublst

    def sublists_product(lst):
        return sublists_product(list(lst), 1) if lst else 1
    return list(set(sublists_with_product_equal_n(circular_list, -87)) | set(circular_sublists_with_product_equal_n(circular_list, -87)))