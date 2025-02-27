def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[n]

def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    fib_48th = fibonacci(47)
    return decimal % fib_48th == 0