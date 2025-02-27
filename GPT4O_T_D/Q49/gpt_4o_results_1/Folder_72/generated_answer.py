from functools import lru_cache

@lru_cache(None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_175th = fib(175)
    return decimal_number % fibonacci_175th == 0