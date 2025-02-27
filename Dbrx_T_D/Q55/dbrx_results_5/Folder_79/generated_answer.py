from itertools import islice, cycle

def sublists_with_product_equal_n(lst, n):
    result = []
    for i in range(len(lst)):
        sublst = [lst[i]]
        for j in range(i, i - len(sublst) - 1, -1):
            sublst.append(lst[j])
            if reduce(lambda x, y: x * y, sublst) == n:
                result.append(sublst)
    return result

def lists_with_product_equal_n(circular_list, n):
    circular_list = list(circular_list)
    result = []
    for i in range(len(circular_list)):
        rotated_list = list(islice(cycle(circular_list[i:] + circular_list[:i]), len(circular_list)))
        result.extend(sublists_with_product_equal_n(rotated_list, n))
    return result