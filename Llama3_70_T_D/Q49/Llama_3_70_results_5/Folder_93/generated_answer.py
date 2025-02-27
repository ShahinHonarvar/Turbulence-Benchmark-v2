def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[-1]

    def binary_to_decimal(binary_str):
        decimal = 0
        for i, bit in enumerate(binary_str[::-1]):
            decimal += int(bit) * 2 ** i
        return decimal
    decimal = binary_to_decimal(binary_str)
    fib_59 = fibonacci(59)
    return decimal % fib_59 == 0