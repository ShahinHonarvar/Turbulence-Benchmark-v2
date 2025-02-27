def return_binary_or_hexa(a_b_tuple):
    """
    Write a function called 'return_binary_or_hexa' that takes one argument, a tuple of distinct nonnegative integers sorted in ascending order.
    Let 'a' denote the integer stored at index 0, and 'b' the integer stored at index 2.
    The function should calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 0 and 2.
    If the sum is an odd number, the function should return the binary representation string of the sum; otherwise, it should return the hexadecimal representation string of the sum.
    The binary representation should not be prefixed with '0b'.
    The hexadecimal representation should not be prefixed with '0x'.
    The binary and hexadecimal representations should start with the most significant digit and have no leading zeros.
    The letters in hexadecimal representation can be either in lowercase or uppercase.
    If all integers from a + 1 to b - 1 (both inclusive) are present in the specified range in the tuple, the function should return an empty string.
    """
    if len(a_b_tuple) != 3 or min(a_b_tuple) < 0 or max(a_b_tuple) != a_b_tuple[2]:
        raise ValueError('Input tuple is not valid')
    a, _, b = a_b_tuple
    missing_numbers = set()
    for i in range(a + 1, b):
        missing_numbers.add(i)
    sum_of_missing_numbers = sum(missing_numbers)
    if sum_of_missing_numbers % 2 != 0:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()