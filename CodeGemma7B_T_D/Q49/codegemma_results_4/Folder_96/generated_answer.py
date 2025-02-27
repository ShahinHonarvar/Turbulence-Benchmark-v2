def if_decimal_is_divisible(binary_representation):
    """
    This function checks if a binary representation is divisible by the 47th number in the Fibonacci sequence.
    The function takes one argument, a binary representation string of a non-negative decimal integer.
    In the given binary representation the most significant digit appears first.
    The function should return true if the decimal integer corresponding to the given string is divisible by the 47th number that occurs in the Fibonacci sequence; otherwise, it should return false.
    The first number that occurs in the Fibonacci sequence is 0.
    """
    decimal_integer = int(binary_representation, 2)
    fibonacci_numbers = []
    fibonacci_numbers.append(0)
    fibonacci_numbers.append(1)
    for i in range(2, 47):
        fibonacci_numbers.append(fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1])
    if decimal_integer % fibonacci_numbers[46] == 0:
        return True
    else:
        return False