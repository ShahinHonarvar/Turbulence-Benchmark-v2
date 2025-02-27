from functools import lru_cache

def fibonacci(n):

    @lru_cache(maxsize=None)
    def fib(i):
        if i == 0:
            return 0
        elif i == 1:
            return 1
        else:
            return fib(i - 1) + fib(i - 2)
    return fib(n)

def is_decimal_divisible_by_fibonacci(bin_string):
    decimal = int(bin_string, 2)
    fibonacci_14 = fibonacci(14)
    return decimal % fibonacci_14 == 0