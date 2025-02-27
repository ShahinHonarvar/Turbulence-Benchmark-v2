def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[n]

def binary_to_decimal(binary):
    decimal = 0
    for i, digit in enumerate(binary[::-1]):
        decimal += int(digit) * 2 ** i
    return decimal

def if_decimal_is_divisible(binary):
    decimal = binary_to_decimal(binary)
    return decimal % fibonacci(47) == 0