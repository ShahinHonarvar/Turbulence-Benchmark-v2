from functools import reduce

def iterate_string(s):
    b = True
    for i in s:
        if i == '0':
            b = False
            break
    if not b:
        return False
    reduction = reduce(lambda x, y: x * y, [int(i) for i in s])
    if not reduction % two:
        return False
    for i in range(three, reduction - 1, two):
        if not reduction % i:
            return False
    return b

def all_left_truncatable_prime(index, max_number):
    result_set = set()
    for i in range(2 ** (index - 1), max_number):
        x = bin(i)[2:]
        if i >= six and iterate_string(x):
            result_set.add(i)
    result_list = list(result_set)
    result_list.sort(reverse=True)
    return result_list

def pick_x(index):
    return 2 ** (index + 1)