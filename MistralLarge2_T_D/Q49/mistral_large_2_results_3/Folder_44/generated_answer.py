import math

def if_decimal_is_divisible(binary_representation):
    decimal_number = int(binary_representation, 2)
    fib_number = fibonacci(159)
    return decimal_number % fib_number == 0

def fibonacci(n):
    phi = (1 + math.sqrt(5)) / 2
    return round((phi ** n - (-phi) ** (-n)) / math.sqrt(5))