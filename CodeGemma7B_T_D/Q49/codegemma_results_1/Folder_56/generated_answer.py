def if_decimal_is_divisible(binary_representation_string):
    decimal_integer = int(binary_representation_string, 2)
    fibonacci_84 = fibonacci(84)
    return decimal_integer % fibonacci_84 == 0

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)