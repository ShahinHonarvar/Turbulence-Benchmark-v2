def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence
    fib_sequence = fibonacci(5)
    decimal = int(binary_string, 2)
    return decimal % fib_sequence[4] == 0