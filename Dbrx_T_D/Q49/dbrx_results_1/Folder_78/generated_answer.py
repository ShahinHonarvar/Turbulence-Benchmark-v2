def is_fibonacci(n):
    return (5 * n * n + 4) % 5 == 0 or (5 * n * n - 4) % 5 == 0

def fibonacci():
    n, m = (0, 1)
    while True:
        yield n
        n, m = (m, n + m)

def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    return is_fibonacci(decimal_number % fib_number)