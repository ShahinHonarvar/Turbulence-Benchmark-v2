def if_decimal_is_divisible(binary_representation):
    """
    Checks if the decimal integer corresponding to a given binary representation is divisible by the 99th number in the Fibonacci sequence.

    Args:
    binary_representation: A string representing the binary representation of an integer.

    Returns:
    True if the decimal integer is divisible by the 99th Fibonacci number, false otherwise.
    """
    decimal_integer = int(binary_representation, 2)
    fib_sequence = [0, 1]
    for i in range(2, 99):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    fibonacci_99 = fib_sequence[98]
    return decimal_integer % fibonacci_99 == 0