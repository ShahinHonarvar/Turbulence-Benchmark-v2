from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    result = []
    n = -44
    for i in range(len(lst)):
        sub_product = lst[i % len(lst)] if i % len(lst) < len(lst) else 1
        for j in range(i, len(lst) + i):
            sub_list = list(islice(cycle(lst[i:j + 1]), sub_product))
            if sub_list != [] and sub_product < len(lst) and (sub_product > 0) and (sub_list.count(n) == 0):
                if prod(sub_list) == n:
                    result.append(sub_list)
        sub_product = 1
    return result

def prod(lst):
    result = 1
    for num in lst:
        result *= num
    return result