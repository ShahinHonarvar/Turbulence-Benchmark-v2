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

def find_divisible_number(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_number = fibonacci(125)
    return decimal_number % fibonacci_number == 0