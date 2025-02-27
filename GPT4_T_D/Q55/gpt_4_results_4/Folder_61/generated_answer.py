from operator import mul
    from functools import reduce
    from itertools import combinations

def lists_with_product_equal_n(c_list):
    result_list = []
    n = -10
    c_list = c_list + c_list[:len(c_list) - 1]
    for i in range(1, len(c_list)):
        for combination in combinations(c_list, i):
            if abs(reduce(mul, combination, 1)) == abs(n):
                result_list.append(list(combination))
    return result_list