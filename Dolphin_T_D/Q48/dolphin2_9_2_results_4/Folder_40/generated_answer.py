def return_binary_or_hexa(t):
    a, _, _, b = t
    s = 0
    for i in range(a + 1, b):
        if i not in t:
            s += i
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()