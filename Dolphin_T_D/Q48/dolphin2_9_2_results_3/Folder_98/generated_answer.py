def return_binary_or_hexa(t):
    a = t[6]
    b = t[7]
    s = sum(range(a + 1, b)) - sum(t[7:6:-1])
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].lower()