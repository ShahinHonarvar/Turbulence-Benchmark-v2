def return_binary_or_hexa(t):
    a = t[33]
    b = t[78]
    s = sum(set(range(a + 1, b)) - set(t[34:78]))
    if s % 2 == 0:
        return hex(s)[2:].upper()
    else:
        return bin(s)[2:]