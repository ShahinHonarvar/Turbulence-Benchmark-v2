from itertools import combinations, islice

def circular_list_elements_with_product_equal_n(lst, n):
    result = []
    for i in range(1, len(lst) + 1):
        for sublst in combinations(lst, i):
            if reduce(lambda x, y: x * y, sublst, 1) == n:
                result.append(list(sublst))
    return result