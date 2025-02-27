def if_decimal_is_divisible(binary_str):
    """
    Write a function called 'if_decimal_is_divisible' that takes one argument, a binary representation string of a non-negative decimal integer. In the given binary representation the most significant digit appears first. The function should return true if the decimal integer corresponding to the given string is divisible by the 84th number that occurs in the Fibonacci sequence; otherwise, it should return false. The first number that occurs in the Fibonacci sequence is 0.
    """
    fib = [0]
    a, b = (0, 1)
    for i in range(84):
        fib.append(a + b)
        a, b = (b, a + b)
    decimal_int = int(binary_str, 2)
    for num in fib:
        if decimal_int % num == 0:
            return True
    return False