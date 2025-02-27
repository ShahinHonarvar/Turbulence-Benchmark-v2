def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

    def binary_to_decimal(binary_string):
        decimal = 0
        for i, bit in enumerate(reversed(binary_string)):
            if bit == '1':
                decimal += 2 ** i
        return decimal
    fib_sequence = fibonacci(127)
    decimal = binary_to_decimal(binary_string)
    return decimal % fib_sequence[126] == 0