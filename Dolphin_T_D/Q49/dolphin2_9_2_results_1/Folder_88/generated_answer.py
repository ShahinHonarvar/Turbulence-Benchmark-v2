def if_decimal_is_divisible(binary_number_string):

    def binary_to_decimal(binary_string):
        binary_to_decimal = 0
        for i in range(len(binary_string)):
            binary_to_decimal += int(binary_string[i]) * pow(2, len(binary_string) - 1 - i)
        return binary_to_decimal

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            fibonacci_sequence = [0, 1]
            for i in range(2, n + 1):
                fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
            return fibonacci_sequence[n]
    decimal_value = binary_to_decimal(binary_number_string)
    fibonacci_49 = fibonacci(49)
    if decimal_value % fibonacci_49 == 0:
        return True
    else:
        return False