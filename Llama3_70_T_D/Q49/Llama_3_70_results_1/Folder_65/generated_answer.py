def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n + 1:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[n]

def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fib_127 = fibonacci(127)
    return decimal_number % fib_127 == 0