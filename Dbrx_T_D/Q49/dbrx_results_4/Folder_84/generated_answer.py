def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_numbers = list(fibonacci())
    if len(fibonacci_numbers) < 196:
        return False
    fib_number = fibonacci_numbers[195]
    return decimal_integer % fib_number == 0