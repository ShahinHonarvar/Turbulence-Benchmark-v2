def if_decimal_is_divisible(binary_str):
    fib_90 = fibonacci(90)
    decimal_value = 0
    for digit in binary_str:
        decimal_value = decimal_value << 1 | int(digit)
    return decimal_value % fib_90 == 0

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)