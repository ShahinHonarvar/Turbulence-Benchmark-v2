def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) < n + 1:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[n]

    def binary_to_decimal(binary_str):
        decimal = 0
        for i, digit in enumerate(binary_str[::-1]):
            decimal += int(digit) * 2 ** i
        return decimal
    decimal = binary_to_decimal(binary_str)
    fib_64 = fibonacci(64)
    return decimal % fib_64 == 0