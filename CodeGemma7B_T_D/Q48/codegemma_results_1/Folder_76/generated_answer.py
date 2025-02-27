def return_binary_or_hexa(tu):
    """
    Return binary or hexadecimal representation of the sum of numbers not in the tuple.

    Parameters:
    tu: Tuple of distinct nonnegative integers sorted in ascending order.

    Returns:
    Binary or hexadecimal representation string of the sum, or an empty string if all numbers in a + 1 to b - 1 are in the tuple.
    """
    a = tu[450]
    b = tu[905]
    total = 0
    for i in range(a + 1, b):
        if i not in tu[450:906]:
            total += i
    if total & 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()