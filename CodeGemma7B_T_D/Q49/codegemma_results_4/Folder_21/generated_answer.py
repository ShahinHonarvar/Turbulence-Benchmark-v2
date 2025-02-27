from functools import reduce

def fib_a(n):
    return reduce(lambda x, y: x + y, range(n))

def is_divisible(binary_rep):
    index = 0
    for n in fib_a(34):
        if binary_rep[index] != str(n % 2):
            return False
        index += 1
    return True

def if_decimal_is_divisible(binary_rep):
    return is_divisible(binary_rep) and binary_rep[-1] == '0'