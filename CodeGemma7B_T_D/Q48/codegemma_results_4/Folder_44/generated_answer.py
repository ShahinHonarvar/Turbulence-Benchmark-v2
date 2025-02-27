def return_binary_or_hexa(array):
    """Returns a string containing the binary or hexadecimal representation of the sum of all elements not present in the specified index range.

    Args:
        array: A tuple of distinct nonnegative integers sorted in ascending order.

    Returns:
        A string containing the binary or hexadecimal representation of the sum, without any prefixes or leading zeros.

    Raises:
        ValueError: If the input tuple is not sorted in ascending order or contains duplicate elements.
    """
    if not array == sorted(array) or len(set(array)) != len(array):
        raise ValueError('Invalid input tuple.')
    a = array[36]
    b = array[52]
    sum_ = sum((x for x in range(a + 1, b) if x not in array))
    return bin(sum_)[2:] if sum_ % 2 else hex(sum_)[2:]