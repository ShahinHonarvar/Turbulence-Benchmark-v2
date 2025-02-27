from functools import reduce

def fibonacci_35():
    return reduce(lambda x, y: x + y, [0, 1] + [x + y for x, y in zip(fib_gen(), fib_gen())][1:])

def fib_gen():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def if_decimal_is_divisible(binary_representation):
    divisible = int(binary_representation, 2) % fibonacci_35() == 0
    return divisible