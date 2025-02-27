def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[-1]
    decimal_int = int(binary_string, 2)
    fib_115 = fibonacci(115)
    return decimal_int % fib_115 == 0