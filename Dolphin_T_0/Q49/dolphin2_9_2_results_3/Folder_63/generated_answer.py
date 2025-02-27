def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def if_decimal_is_divisible(bin_str):
    return fibonacci(143) % int(bin_str, 2) == 0