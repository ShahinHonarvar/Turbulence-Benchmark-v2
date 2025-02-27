def is_fibonacci(n):
    return n > 0 and ((5 * n * n - 4) % 10 == 0 or (5 * n * n + 4) % 10 == 0)

def fibonacci():
    n, m = (0, 1)
    while True:
        yield n
        n, m = (m, n + m)

def if_decimal_is_divisible(binary_representation):
    decimal_number = int(binary_representation, 2)
    fibonacci_sequence = fibonacci()
    for _ in range(27):
        fibonacci_number = next(fibonacci_sequence)
        if is_fibonacci(fibonacci_number) and (fibonacci_number == 0 or decimal_number % fibonacci_number == 0):
            return True
    return False