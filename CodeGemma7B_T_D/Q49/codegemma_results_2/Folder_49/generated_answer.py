def binary_to_decimal(binary_str):
    decimal = 0
    for i in range(len(binary_str)):
        decimal += int(binary_str[i]) * 2 ** (len(binary_str) - i - 1)
    return decimal

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def if_decimal_is_divisible(binary_str):
    decimal = binary_to_decimal(binary_str)
    fib_95 = fibonacci(95)
    return decimal % fib_95 == 0