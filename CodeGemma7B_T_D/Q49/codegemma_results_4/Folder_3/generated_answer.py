def if_decimal_is_divisible(binary):
    fibonacci_35 = fibonacci(35)
    decimal = int(binary, 2)
    return decimal % fibonacci_35 == 0

def fibonacci(n):
    if n in [1, 2]:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)