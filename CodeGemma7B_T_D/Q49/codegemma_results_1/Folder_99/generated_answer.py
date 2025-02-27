from functools import partial

def binary_to_decimal(binary):
    """Converts a binary representation string to a decimal integer."""
    return int(binary, 2)

def decimal_to_binary(decimal):
    """Converts a decimal integer to a binary representation string."""
    return bin(decimal)[2:]

def n_th_fibonacci(n):
    """Computes the nth number in the Fibonacci sequence."""
    if n < 2:
        return n
    return n_th_fibonacci(n - 1) + n_th_fibonacci(n - 2)

def if_decimal_is_divisible(binary):
    """Checks if the decimal integer corresponding to a given binary string is divisible by the 109th number that occurs in the Fibonacci sequence. Return true if it is divisible, false otherwise."""
    binary_size = len(binary)
    if binary_size > 34:
        binary = binary[:34]
    decimal = binary_to_decimal(binary)
    computed_fibonacci = n_th_fibonacci(109)
    if decimal % computed_fibonacci == 0:
        return True
    return False