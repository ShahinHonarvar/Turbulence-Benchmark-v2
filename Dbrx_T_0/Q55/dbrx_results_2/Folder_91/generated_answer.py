from itertools import islice, cycle

def lists_with_product_equal_n(lst):

    def sublists_with_product_equal_n(lst, n):
        result = []
        current_product = 1
        for i, j in zip(lst, cycle(lst[len(lst) // 2:])):
            current_product *= i
            if current_product == n:
                result.append(lst[:j])
                current_product = 1
            elif current_product > n:
                current_product = 1
        return result
    return sublists_with_product_equal_n(lst, 2) or sublists_with_product_equal_n(lst, -2)