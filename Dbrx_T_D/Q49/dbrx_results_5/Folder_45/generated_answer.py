import functools

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def is_divisible_by_fibonacci(n, fib_number):
    return n % fib_number == 0

@functools.lru_cache(maxsize=None)
def to_decimal(bstring):
    if len(bstring) == 0:
        return 0
    else:
        return 2 * to_decimal(bstring[1:]) + int(bstring[0])

def if_decimal_is_divisible(bstring):
    decimal_number = to_decimal(bstring)
    fib_number = fibonacci(28)
    return is_divisible_by_fibonacci(decimal_number, fib_number)