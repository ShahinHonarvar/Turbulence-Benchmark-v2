def if_decimal_is_divisible(binary_string):

    def generate_fibonacci_sequence(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

    def binary_to_decimal(binary_string):
        decimal = 0
        for i, bit in enumerate(binary_string[::-1]):
            decimal += int(bit) * 2 ** i
        return decimal
    fib_sequence = generate_fibonacci_sequence(138)
    decimal = binary_to_decimal(binary_string)
    return decimal % fib_sequence[137] == 0