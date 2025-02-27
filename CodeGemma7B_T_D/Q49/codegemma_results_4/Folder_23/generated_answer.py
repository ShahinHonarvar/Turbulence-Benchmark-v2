def if_decimal_is_divisible(binary_number):
    fib_gen = fibonacci()
    decimal_number = int(binary_number, 2)
    for fibonacci_number in fib_gen:
        if decimal_number % fibonacci_number == 0:
            return True
    return False

def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)