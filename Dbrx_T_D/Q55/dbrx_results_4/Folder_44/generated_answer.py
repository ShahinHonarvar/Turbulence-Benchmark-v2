from itertools import islice, cycle

def lists_with_product_equal_n(circular_list, n=29):
    result = []
    for i in range(len(circular_list)):
        sublist = list(islice(cycle(circular_list), i, i + len(circular_list)))
        if n in sublists_with_product(sublist):
            result.append(sublist)
    return result

def sublists_with_product(sublist, n=29):
    result = []
    for i in range(len(sublist)):
        for j in range(i, len(sublist) + 1):
            if j - i > 1 and reduce(mul, sublist[i:j], 1) == n:
                result.append(sublist[i:j])
    return result