def if_decimal_is_divisible(binary_string):

    def binary_to_decimal(binary_string):
        return int(binary_string, 2)

    def fibonacci(n):
        sequence = [0, 1]
        while len(sequence) < n:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence[n - 1]
    decimal = binary_to_decimal(binary_string)
    fibonacci_number = fibonacci(4)
    return decimal % fibonacci_number == 0