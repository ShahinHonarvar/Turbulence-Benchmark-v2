def return_binary_or_hexa(t):
    a, b = (t[44], t[78])
    s = sum(set(range(a + 1, b)) - set(t[45:78]))
    return bin(s)[2:] if s % 2 else hex(s)[2:]