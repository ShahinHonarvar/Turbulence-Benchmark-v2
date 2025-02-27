def if_decimal_is_divisible(binary_string):

    def fibonacci_sequence(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) < n + 1:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[n]
    decimal = int(binary_string, 2)
    fib_139 = fibonacci_sequence(139)
    return decimal % fib_139 == 0