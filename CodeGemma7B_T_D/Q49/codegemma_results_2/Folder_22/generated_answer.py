def if_decimal_is_divisible(binary_string):
    """
    Write a function called 'if_decimal_is_divisible' that takes one argument, a binary representation string of a non-negative decimal integer.
    In the given binary representation the most significant digit appears first.
    The function should return true if the decimal integer corresponding to the given string is divisible by the 20th number that occurs in the Fibonacci sequence; otherwise, it should return false.
    The first number that occurs in the Fibonacci sequence is 0.
    """
    fib = [0, 1]
    for i in range(2, 20):
        fib.append(fib[i - 1] + fib[i - 2])
    decimal_int = int(binary_string, 2)
    if decimal_int % fib[19] == 0:
        return True
    else:
        return False