def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) < n + 1:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[n]

    def binary_to_decimal(binary_str):
        decimal = 0
        for char in binary_str:
            decimal = decimal * 2 + int(char)
        return decimal
    decimal = binary_to_decimal(binary_str)
    fib_199 = fibonacci(199)
    return decimal % fib_199 == 0