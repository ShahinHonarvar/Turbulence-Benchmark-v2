def if_decimal_is_divisible(binary_representation):
    """
    This function takes one argument, a binary representation string of a non-negative decimal integer. In the given binary representation the most significant digit appears first. The function should return true if the decimal integer corresponding to the given string is divisible by the 198th number that occurs in the Fibonacci sequence; otherwise, it should return false. The first number that occurs in the Fibonacci sequence is 0.
    """

    def fibonacci_number(limit):
        fib_sequence = [0, 1]
        while fib_sequence[-1] <= limit:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[-2]

    def convert_binary_to_decimal(binary_representation):
        decimal_value = 0
        for i, digit in enumerate(binary_representation):
            decimal_value += int(digit) * 2 ** (len(binary_representation) - i - 1)
        return decimal_value
    '\n    Fibonacci sequence\n    '
    current_fibonacci = fibonacci_number(3000)
    '\n    Convert binary string to decimal integer\n    '
    decimal_integer = convert_binary_to_decimal(binary_representation)
    '\n    Check if the decimal integer is divisible by the 198th number in the Fibonacci sequence\n    '
    if decimal_integer % current_fibonacci == 0:
        return True
    else:
        return False