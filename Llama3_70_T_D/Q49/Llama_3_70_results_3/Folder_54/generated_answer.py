def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[-1]

def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fib_34 = fibonacci(34)
    return decimal_number % fib_34 == 0