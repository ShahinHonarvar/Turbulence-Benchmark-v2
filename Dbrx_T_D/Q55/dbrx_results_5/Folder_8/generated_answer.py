from itertools import combinations

def lists_with_product_equal_n(circular_list):

    def is_contiguous(sublist):
        return len(sublist) == 1 or any((sublist[i] + 1 == sublist[i + 1] for i in range(len(sublist) - 1)))

    def sublists_with_product_equal_n(lst, n):
        result = []
        for i in range(1, len(lst) + 1):
            for j in combinations(lst, i):
                if is_contiguous(j) and product(j) == n:
                    result.append(list(j))
        return result

    def product(lst):
        return reduce(lambda x, y: x * y, lst, 1)
    return sublists_with_product_equal_n(circular_list + [circular_list[0]], -41)