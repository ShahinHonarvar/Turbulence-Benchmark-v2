def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def if_decimal_is_divisible(binary_string):
    fib_126 = fibonacci(126)[-1]
    decimal = int(binary_string, 2)
    return decimal % fib_126 == 0