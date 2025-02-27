def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def fibonacci_number(index):
    for i, num in enumerate(fibonacci()):
        if i == index:
            return num

def is_decimal_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    return decimal_number % fibonacci_number(199) == 0 if decimal_number else True