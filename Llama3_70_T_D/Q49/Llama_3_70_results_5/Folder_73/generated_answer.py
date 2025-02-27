def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_164 = fibonacci(165)[164]
    return decimal % fib_164 == 0