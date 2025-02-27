def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[-1]
    decimal_integer = int(binary_string, 2)
    fibonacci_24 = fibonacci(24)
    return decimal_integer % fibonacci_24 == 0