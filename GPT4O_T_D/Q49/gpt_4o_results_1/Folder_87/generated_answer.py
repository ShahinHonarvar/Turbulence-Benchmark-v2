def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        fib_sequence = [0, 1]
        for i in range(2, n + 1):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[n]
    fib_180 = fibonacci(180)
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_180 == 0