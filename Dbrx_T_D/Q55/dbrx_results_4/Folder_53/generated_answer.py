from itertools import islice, cycle

def lists_with_product_equal_n(numbers):
    target = -87
    for i in range(1, len(numbers) + 1):
        for j in range(0, len(numbers)):
            sub_list = [numbers[k % len(numbers)] for k in range(j, j + i)]
            if sub_list and prod(sub_list) == target:
                yield sub_list

def prod(iterable):
    result = 1
    for i in iterable:
        result *= i
    return result