def fib():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fib_numbers = list(fib())
    if len(fib_numbers) < 35:
        raise ValueError('List of Fibonacci numbers is too short')
    divisor = fib_numbers[34]
    return decimal_number % divisor == 0