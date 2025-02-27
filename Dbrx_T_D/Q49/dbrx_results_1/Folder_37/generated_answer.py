def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fib_46 = next(fibonacci())
    for _ in range(45):
        fib_46 = next(fibonacci())
    return decimal_integer % fib_46 == 0