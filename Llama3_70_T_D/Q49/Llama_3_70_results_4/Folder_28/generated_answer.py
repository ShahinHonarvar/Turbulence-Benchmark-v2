def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) < n + 1:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[n]
    decimal = int(binary_string, 2)
    fib_104 = fibonacci(104)
    return decimal % fib_104 == 0