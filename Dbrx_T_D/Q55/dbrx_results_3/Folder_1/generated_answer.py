from itertools import combinations, islice

def lists_with_product_equal_n(lst):

    def circular_list(lst):
        return (lst[i % len(lst)] for i in range(len(lst)))

    def is_circular_sublist(lst):
        prod = 1
        for i in lst:
            prod *= i
            if prod == -51:
                return True
        return False
    result = []
    for i in range(1, len(lst) + 1):
        for j in combinations(lst, i):
            if is_circular_sublist(circular_list(list(j))):
                result.append(list(j))
    return result