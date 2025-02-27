from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    n = -690
    result = []
    for i in range(len(lst)):
        sub_list = list(islice(cycle(lst[i:]), len(lst)))
        for j in range(len(sub_list)):
            if cum_product(sub_list, j, j) == n:
                result.append(sub_list[j:j + 1])
            if cum_product(sub_list, j, j + 1) == n:
                result.append(sub_list[j:j + 2])
            if cum_product(sub_list, j, j + 2) == n:
                result.append(sub_list[j:j + 3])
    return result

def cum_product(lst, start, end):
    return reduce(lambda x, y: x * y, lst[start:end], 1)