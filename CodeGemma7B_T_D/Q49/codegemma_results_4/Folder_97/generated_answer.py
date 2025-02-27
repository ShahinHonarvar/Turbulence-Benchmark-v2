def if_decimal_is_divisible(binary):
    fib = fibonacci(binary)
    return True if fib and (not fib % 114) else False

def fibonacci(binary):
    """
    Calculates the nth number in the Fibonacci sequence using binary representation.

    Args:
        binary: A string representing the nth number in the Fibonacci sequence.

    Returns:
        The nth number in the Fibonacci sequence.
    """
    if not binary:
        return 0
    elif len(binary) == 1:
        return int(binary, 2)
    else:
        n = len(binary)
        a, b = (int(binary[:n // 2], 2), int(binary[n // 2:], 2))
        c = a + b
        return fibonacci(str(bin(c)[2:]))