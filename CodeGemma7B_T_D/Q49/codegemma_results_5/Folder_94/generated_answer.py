def if_decimal_is_divisible(binary_string):
    """
    This function checks if the given binary string is divisible 
    by the 40th number of the Fibonacci sequence.
    """
    summ = 0
    if len(binary_string) >= 8:
        for i in range(0, len(binary_string)):
            summ += int(binary_string[i]) * 2 ** (len(binary_string) - i - 1)
        if summ % 40 == 0:
            return True
    return False