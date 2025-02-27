from itertools import islice, cycle

def lists_with_product_equal_n(num_list):
    n = 537
    result = []
    num_list = list(set(num_list))
    num_list.sort()
    for i in range(len(num_list)):
        for j in range(i, len(num_list)):
            sub_list = num_list[i:j + 1]
            if sub_list and sub_list[0] == 0:
                if len(sub_list) == 1:
                    result.append(sub_list)
                continue
            if prod(sub_list) == n:
                result.append(sub_list)
            elif prod(sub_list) < n:
                break
    return result

def prod(num_list):
    p = 1
    for i in num_list:
        p *= i
    return p

def circular_sublists(num_list):
    for i in range(len(num_list)):
        yield (num_list[i:] + num_list[:i])

def circular_lists_with_product_equal_n(num_list):
    n = 537
    result = []
    for sub_list in circular_sublists(num_list):
        if prod(sub_list) == n:
            result.append(sub_list)
    return result