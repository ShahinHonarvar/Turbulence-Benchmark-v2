def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[n - 1]
    decimal_num = int(binary_str, 2)
    fib_38 = fibonacci(38)
    return decimal_num % fib_38 == 0