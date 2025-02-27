from functools import lru_cache

def fibonacci(n):

    @lru_cache(maxsize=None)
    def fib(num):
        if num < 2:
            return num
        else:
            return fib(num - 1) + fib(num - 2)
    return fib(n)

def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    fibonacci_num = fibonacci(48)
    if decimal_num % fibonacci_num == 0:
        return True
    else:
        return False