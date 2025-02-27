def fib(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n + 1:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[n]

def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_number = fib(45)
    return decimal % fibonacci_number == 0