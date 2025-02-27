from itertools import islice, cycle

def lists_with_product_equal_n(lst, n=85):

    def product_equals_n(sublist):
        return len(sublist) > 0 and len(list(filter(lambda x: x != 1, sublist))) <= 1 and (abs(reduce(lambda x, y: x * y, sublist)) == 85)

    def circular_sublists(lst):
        for i in range(1, len(lst) // 2 + 1):
            yield from (lst[0:j] + sublist for j in range(i, len(lst) - i + 1) for sublist in islice(circular_sublists(lst[i:j]), 2))
    return [sublist for sublist in circular_sublists(lst) if product_equals_n(sublist)]