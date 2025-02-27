from itertools import islice, cycle

def lists_with_product_equal_n(lst):

    def sublists_with_product_equal_n(lst, n):
        result = []
        product = 1
        for i, j in zip(lst, cycle(lst[len(lst) // 2 + 1:])):
            product *= i
            while product > n:
                product //= next(islice(lst, len(lst) // 2, None))
            if product == n:
                result.append([x for x in islice(lst, len(lst) // 2, None)])
        return result
    return sublists_with_product_equal_n(lst, 537) + sublists_with_product_equal_n(lst[::-1], 537)