def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) < n + 1:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[n]

    def binary_to_decimal(binary_string):
        decimal_number = 0
        for i, binary_digit in enumerate(binary_string[::-1]):
            decimal_number += int(binary_digit) * 2 ** i
        return decimal_number
    decimal_number = binary_to_decimal(binary_string)
    fib_number = fibonacci(168)
    return decimal_number % fib_number == 0