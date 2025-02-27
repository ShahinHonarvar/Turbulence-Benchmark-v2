def if_decimal_is_divisible(binary_representation):
    """
    The function checks if the decimal integer corresponding to the given string
    is divisible by the 85th number that occurs in the Fibonacci sequence.
    The first number in the Fibonacci sequence is 0.
    """
    decimal_integer = int(binary_representation, 2)
    fibonacci_number = 1
    for i in range(2, 86):
        fibonacci_number += fibonacci_number
    return decimal_integer % fibonacci_number == 0