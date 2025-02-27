def if_decimal_is_divisible(binary_representation):
    """
    Calculates the decimal value of a binary representation string.

    Args:
        binary_representation: A string containing the binary representation of a decimal integer.

    Returns:
        The decimal value of the binary representation.
    """
    decimal_value = 0
    for i, bit in enumerate(binary_representation):
        decimal_value += int(bit) * 2 ** i
    return decimal_value

def fibonacci(n):
    """
    Calculates the nth number in the Fibonacci sequence.

    Args:
        n: The index of the Fibonacci number to calculate.

    Returns:
        The nth Fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def is_divisible_by_fibonacci(binary_representation):
    """
    Checks if the decimal integer corresponding to a binary representation is divisible by the 19th Fibonacci number.

    Args:
        binary_representation: A string containing the binary representation of a decimal integer.

    Returns:
        True if the decimal integer is divisible by the 19th Fibonacci number, False otherwise.
    """
    decimal_value = if_decimal_is_divisible(binary_representation)
    fibonacci_number = fibonacci(19)
    return decimal_value % fibonacci_number == 0