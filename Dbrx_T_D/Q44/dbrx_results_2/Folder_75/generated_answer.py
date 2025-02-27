from math import sqrt

def is_composite(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(input_list):
    result = set()
    for i in range(75, 86):
        if is_composite(input_list[i]):
            result.add(input_list[i])
    return result