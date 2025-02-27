def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def binary_to_decimal(binary_string):
    return int(binary_string, 2)

def fibonacci_number(n):
    for i, num in enumerate(fibonacci()):
        if i == n:
            return num

def if_decimal_is_divisible(binary_string):
    decimal_number = binary_to_decimal(binary_string)
    fibonacci_24 = fibonacci_number(24)
    return decimal_number % fibonacci_24 == 0