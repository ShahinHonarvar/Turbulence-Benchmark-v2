def return_binary_or_hexa(t):
    """
    Returns the binary or hexadecimal representation of the sum of all integers between
    a + 1 and b - 1 that are not present in the tuple t between indices 36 and 85.
    """
    a, b = (t[36], t[85])
    s = 0
    for i in range(a + 1, b):
        if i not in t[36:86]:
            s += i
    return bin(s)[2:] if s % 2 else hex(s)[2:].upper()