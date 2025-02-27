def return_binary_or_hexa(t):
    a, b = (t[200], t[202])
    missing_numbers = set(range(a + 1, b)) - set(t[200:203])
    s = sum(missing_numbers)
    return bin(s)[2:] if s % 2 else hex(s)[2:]