from functools import lru_cache

def fibonacci(n):

    @lru_cache(maxsize=None)
    def fib(i):
        if i < 2:
            return i
        else:
            return fib(i - 1) + fib(i - 2)
    return fib(n)

def to_decimal(binary_string):
    return int(binary_string, 2)

def if_decimal_is_divisible(binary_string):
    decimal_number = to_decimal(binary_string)
    fibonacci_number = fibonacci(160)
    return decimal_number % fibonacci_number == 0