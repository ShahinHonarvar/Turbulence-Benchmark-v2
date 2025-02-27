from math import sqrt

def if_decimal_is_divisible(string):

    def fibonacci(a, b):
        return (b, a + b)
    b, a = fibonacci(0, 1)
    fib, number = (a, 2)
    while fib <= int(sqrt(a * a + b * b)):
        number -= 1
        if number != 0:
            b, a = fibonacci(a, b)
            fib, _ = fibonacci(fib, a)
        elif number == 0:
            fib, b = fibonacci(fib, b)
    return int(string, 2) % fib == 0