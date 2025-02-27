def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence
    fib_sequence = fibonacci(171)
    decimal = int(binary_representation, 2)
    return decimal % fib_sequence[170] == 0