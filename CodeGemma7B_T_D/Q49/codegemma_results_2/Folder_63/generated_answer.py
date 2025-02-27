from functools import reduce

def get_fib(num):
    fib = [0, 1]
    for i in range(2, num):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib

def binary_to_decimal(binary):
    return reduce(lambda x, y: x * 2 + y, map(int, reversed(binary)))

def is_divisible_by_144th_fib_num(binary):
    fib_nums = get_fib(144)
    if binary_to_decimal(binary) % fib_nums[144 - 1] == 0:
        return True
    return False