def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n + 1:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[n]

def if_decimal_is_divisible(binary_string):
    decimal = sum((int(digit) * 2 ** index for index, digit in enumerate(reversed(binary_string))))
    return decimal % fibonacci(84) == 0