def if_decimal_is_divisible(binary_representation):
    """
    Write a function called 'if_decimal_is_divisible' that takes one argument, a binary representation string of a non-negative decimal integer.
    In the given binary representation the most significant digit appears first.
    The function should return true if the decimal integer corresponding to the given string is divisible by the 19th number that occurs in the Fibonacci sequence; otherwise, it should return false.
    The first number that occurs in the Fibonacci sequence is 0.
    """
    decimal = int(binary_representation, 2)
    fib_list = [0, 1]
    while len(fib_list) < 20:
        fib_list.append(fib_list[-1] + fib_list[-2])
    if decimal % fib_list[19] == 0:
        return True
    else:
        return False