def if_decimal_is_divisible(binary_str):

    def binary_to_decimal(binary):
        return int(binary, 2)

    def fibonacci(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) <= n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[n]
    decimal_value = binary_to_decimal(binary_str)
    fib_85th = fibonacci(85)
    return decimal_value % fib_85th == 0