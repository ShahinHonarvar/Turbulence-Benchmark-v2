def if_decimal_is_divisible(binary):
    fibonacci_190 = fibonacci(190)
    decimal = int(binary, 2)
    return decimal % fibonacci_190 == 0

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)