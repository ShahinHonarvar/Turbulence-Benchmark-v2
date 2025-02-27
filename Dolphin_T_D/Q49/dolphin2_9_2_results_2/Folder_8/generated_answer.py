def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    for i in range(2, n + 1):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return fib_sequence

def binary_to_decimal(binary):
    decimal = 0
    for i in range(len(binary)):
        decimal = decimal + int(binary[len(binary) - i - 1]) * pow(2, i)
    return decimal

def if_decimal_is_divisible(binary):
    decimal = binary_to_decimal(binary)
    fib_sequence = fibonacci_sequence(54)
    return decimal % fib_sequence[53] == 0