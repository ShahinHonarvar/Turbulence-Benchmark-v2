def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)

    def fibonacci(n):
        fib_sequence = [0, 1]
        for i in range(2, n + 1):
            fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
        return fib_sequence[n]
    fib_67 = fibonacci(67)
    return decimal_number % fib_67 == 0