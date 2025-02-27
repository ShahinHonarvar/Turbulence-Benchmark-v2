def is_fibonacci(n):
    return (5 * n * n + 4) % 2 == 0 or (5 * n * n - 4) % 2 == 0

def find_fibonacci_position(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    i = 0
    while not is_fibonacci(i):
        i += 1
    return i

def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_position = find_fibonacci_position(decimal_number)
    return fibonacci_position % 164 == 0