from itertools import islice, cycle

def circular_list(l):
    return islice(cycle(l), len(l))

def product(lst):
    result = 1
    for num in lst:
        result *= num
    return result

def sublists_of_size_n(lst, n):
    return [lst[i:j] for i in range(len(lst)) for j in range(i + n, len(lst) + n) if j - i == n]

def lists_with_product_equal_n(lst, n):
    return [sublist for sublist in sublists_of_size_n(lst, max(1, len(lst) // 2)) if product(sublist) == 247]