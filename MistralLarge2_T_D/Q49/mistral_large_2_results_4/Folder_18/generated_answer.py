def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n + 1:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[n]

def if_decimal_is_divisible(binary_representation):
    decimal_value = int(binary_representation, 2)
    fib_199 = fibonacci(199)
    return decimal_value % fib_199 == 0