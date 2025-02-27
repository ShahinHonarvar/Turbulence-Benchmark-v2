def is_fibonacci(n):
    return (5 * n ** 2 + 4) % (50 * n ** 2 - 20 * n + 4) == 0 or (5 * n ** 2 - 4) % (50 * n ** 2 - 20 * n + 4) == 0

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[-1]

def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    if is_fibonacci(fibonacci(14)):
        return decimal_integer % fibonacci(14) == 0
    else:
        return False