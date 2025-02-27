def return_binary_or_hexa(tup):
    """
            Write a function called 'return_binary_or_hexa' that takes one argument, a tuple of distinct nonnegative integers sorted in ascending order. Let 'a' denote the integer stored at index 30, and 'b' the integer stored at index 200. The function should calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 30 and 200. If the sum is an odd number, the function should return the binary representation string of the sum; otherwise, it should return the hexadecimal representation string of the sum. The binary representation should not be prefixed with '0b'. The hexadecimal representation should not be prefixed with '0x'. The binary and hexadecimal representations should start with the most significant digit and have no leading zeros. The letters in hexadecimal representation can be either in lowercase or uppercase. If all integers from a + 1 to b - 1 (both inclusive) are present in the specified range in the tuple, the function should return an empty string.
            """
    a, b = (tup[30], tup[200])
    result = 0
    for i in range(a + 1, b):
        if tup.index(i) == -1:
            result += i
    if result % 2 == 0:
        return hex(result)[2:]
    else:
        return bin(result)[2:]