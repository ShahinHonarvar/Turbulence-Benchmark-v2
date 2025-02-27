def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[-1]

def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_109 = fibonacci(109)
    return decimal % fibonacci_109 == 0