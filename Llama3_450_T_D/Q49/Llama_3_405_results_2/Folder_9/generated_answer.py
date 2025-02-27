def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[n - 1]
    decimal_int = int(binary_str, 2)
    fib_68 = fibonacci(68)
    return decimal_int % fib_68 == 0