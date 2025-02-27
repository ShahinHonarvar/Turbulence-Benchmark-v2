def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[-1]

def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_100 = fibonacci(100)
    return decimal % fib_100 == 0