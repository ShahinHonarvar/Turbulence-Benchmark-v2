from functools import lru_cache

def fibonacci(n):

    @lru_cache
    def fib_internal(n):
        if n < 2:
            return n
        return fib_internal(n - 1) + fib_internal(n - 2)
    return fib_internal(n)

def to_decimal(binary_string):
    return int(binary_string, 2)

def is_fib_divisible(binary_string):
    decimal_number = to_decimal(binary_string)
    fib_number = fibonacci(40)
    return decimal_number % fib_number == 0