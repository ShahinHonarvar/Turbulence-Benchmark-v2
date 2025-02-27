def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    if fibonacci().__next__() % 175 != 0:
        fibonacci().__next__()
    return fibonacci().__next__() % decimal_number == 0