def if_decimal_is_divisible(binary_representation):
    """Write a function called 'if_decimal_is_divisible' that takes one argument, a binary representation string of a non-negative decimal integer. In the given binary representation the most significant digit appears first. The function should return true if the decimal integer corresponding to the given string is divisible by the 110th number that occurs in the Fibonacci sequence; otherwise, it should return false. The first number that occurs in the Fibonacci sequence is 0."""
    fib = [0, 1]
    for i in range(110):
        fib.append(fib[i] + fib[i + 1])
    decimal = int('0b' + binary_representation, 2)
    if decimal in fib:
        return True
    return False