import math

def fibonacci(n):
    phi = (1 + math.sqrt(5)) / 2
    return int(round(pow(phi, n) / math.sqrt(5)))

def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_number = fibonacci(198)
    return decimal_number % fibonacci_number == 0