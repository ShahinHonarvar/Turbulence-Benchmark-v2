def return_binary_or_hexa(n):
    """
    (tuple[int]) -> str

    Returns the binary or hexadecimal representation of the sum of all integers from n[1] + 1 to n[7] - 1 (inclusive) that are not present in the tuple. If all integers from n[1] + 1 to n[7] - 1 (inclusive) are present in the tuple, the function returns an empty string.

    Example:
    >>> return_binary_or_hexa((87, 12, 345, 678, 901, 23, 567, 89))
    '101'
    >>> return_binary_or_hexa((87, 12, 345, 678, 901, 23, 567, 90))
    '45'
    """
    nums = set(n[1:8])
    total = sum((i for i in range(n[1] + 1, n[7] + 1) if i not in nums))
    return bin(total)[2:] if total % 2 else hex(total)[2:].upper()