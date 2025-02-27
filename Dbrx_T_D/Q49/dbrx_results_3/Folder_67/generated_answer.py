def is_fibonacci(n):
    return n > 0 and (5 * n * n - 4) % 10 == 0 or (5 * n * n + 4) % 10 == 0

def fibonacci_position(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a, b, c = (0, 1, 2)
        for _ in range(n - 3):
            a, b, c = (b, c, (b + c) % 10)
        return c

def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    if is_fibonacci(fibonacci_position(decimal_integer)):
        return decimal_integer % 107 == 0
    else:
        return False