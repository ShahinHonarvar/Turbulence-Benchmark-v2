def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    return decimal % fibonacci(105) == 0

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)