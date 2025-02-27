def if_decimal_is_divisible(binary_representation):
    """
    Returns True if the decimal integer corresponding to the given string
    is divisible by the 6th number that occurs in the Fibonacci sequence;
    otherwise, it returns False.
    """
    decimal_integer = int(binary_representation, 2)
    fibonacci_sequence = [0, 1]
    for i in range(2, 6):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    if decimal_integer % fibonacci_sequence[5] == 0:
        return True
    else:
        return False