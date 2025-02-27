def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_numbers = list(fibonacci())
    twentieth_fibonacci_number = fibonacci_numbers[19]
    return decimal_number % twentieth_fibonacci_number == 0