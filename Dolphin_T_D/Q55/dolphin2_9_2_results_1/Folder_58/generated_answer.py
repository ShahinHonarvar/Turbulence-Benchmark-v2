from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    if len(lst) < 1:
        return []
    result = []
    lst_cycle = cycle(lst)
    for i in range(len(lst)):
        current_list = [next(lst_cycle) for _ in range(i + 1)]
        product = 1
        for num in current_list:
            product *= num
        if product == 733:
            result.append(list(current_list))
    return result