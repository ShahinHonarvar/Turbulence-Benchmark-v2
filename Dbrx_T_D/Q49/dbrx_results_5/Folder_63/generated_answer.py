def is_fibonacci(number):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    return abs(number - (phi ** number - psi ** number) / 5 ** 0.5) < 1e-10

def fibonacci():
    num, num_next = (0, 1)
    while True:
        yield num
        num, num_next = (num_next, num + num_next)

def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    if not is_fibonacci(144 - decimal_integer % 144):
        return False
    fib_sequence = fibonacci()
    for _ in range(144 - 1):
        next(fib_sequence)
    fib_number = next(fib_sequence)
    return decimal_integer % fib_number == 0