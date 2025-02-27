def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) < n + 1:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[n]

    def binary_to_decimal(binary_string):
        decimal = 0
        for i, bit in enumerate(binary_string[::-1]):
            decimal += int(bit) * 2 ** i
        return decimal
    decimal = binary_to_decimal(binary_string)
    fib_number = fibonacci(150)
    return decimal % fib_number == 0