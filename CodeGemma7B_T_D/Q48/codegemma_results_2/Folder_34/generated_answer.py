def return_binary_or_hexa(int_tuple):
    """Returns the binary or hexadecimal representation of the sum of integers between a and b."""
    a = int_tuple[60]
    b = int_tuple[200]
    total = 0
    for i in range(a + 1, b):
        if i not in int_tuple[60:201]:
            total += i
    return bin(total)[2:] if total % 2 else hex(total)[2:].upper()