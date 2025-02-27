def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def is_decimal_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_numbers = list(itertools.islice(fibonacci(), 87))
    return decimal_integer % fibonacci_numbers[-1] == 0