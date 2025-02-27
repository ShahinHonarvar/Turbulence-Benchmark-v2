def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        a, b = (b, a + b)

def is_divisible_by_185th_fibonacci_number(binary_string):
    decimal_number = int(binary_string, 2)
    fib_sequence = list(fibonacci())
    if len(fib_sequence) < 185:
        raise ValueError('Generated only {0} Fibonacci numbers, but required 185'.format(len(fib_sequence)))
    return decimal_number % fib_sequence[184] == 0