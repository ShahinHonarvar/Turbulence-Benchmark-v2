def return_binary_or_hexa(num_tuple):
    """
    Calculates the sum of integers outside a given tuple and returns the binary or hexadecimal representation.

    Args:
    num_tuple: A tuple of distinct nonnegative integers sorted in ascending order.

    Returns:
    The binary or hexadecimal representation of the sum, depending on whether it's odd or even.
    """
    a = num_tuple[3]
    b = num_tuple[9]
    sum = 0
    for i in range(a + 1, b):
        if i not in num_tuple[3:10]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()