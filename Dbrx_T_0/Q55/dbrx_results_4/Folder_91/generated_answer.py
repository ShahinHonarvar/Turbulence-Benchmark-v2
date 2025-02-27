from itertools import islice, cycle

def lists_with_product_equal_n(lst):

    def sublists_with_product_equal_n(lst, n):
        result = []
        for i in range(len(lst)):
            for j in range(i, len(lst)):
                if lst[i:j + 1] and product(lst[i:j + 1]) == n:
                    result.append(lst[i:j + 1])
        return result

    def product(lst):
        return reduce(lambda x, y: x * y, lst, 1)
    return sublists_with_product_equal_n(lst, 2) + sublists_with_product_equal_n(lst, -2)

def circular_sublists(lst, size):
    return [lst[i:j] for i in range(len(lst)) for j in range(i + 1, i + size + 1) if j <= len(lst)]

def circular_sublists_with_product_equal_n(lst, n):
    return [sublist for sublist in circular_sublists(lst, len(lst)) if product(sublist) == n]

def circular_lists_with_product_equal_n(lst):
    return circular_sublists_with_product_equal_n(lst, 2) + circular_sublists_with_product_equal_n(lst, -2)

def circular_sublists_with_product_equal_n_recursive(lst, n, i=0, acc=[]):
    if i == len(lst):
        return [acc] if product(acc) == n else []
    result = []
    if product(acc) * lst[i] == n:
        result.append(acc + [lst[i]])
    if product(acc) * lst[i] < n:
        result.extend(circular_sublists_with_product_equal_n_recursive(lst, n, i + 1, acc + [lst[i]]))
    result.extend(circular_sublists_with_product_equal_n_recursive(lst, n, i + 1, acc))
    return result

def circular_lists_with_product_equal_n_recursive(lst):
    return circular_sublists_with_product_equal_n_recursive(lst, 2) + circular_sublists_with_product_equal_n_recursive(lst, -2)