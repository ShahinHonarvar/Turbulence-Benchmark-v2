def return_binary_or_hexa(t):
    a = t[44]
    b = t[78]
    s = 0
    for i in range(a + 1, b):
        if i not in t[45:78]:
            s += i
    if s % 2 == 0:
        return hex(s)[2:].upper()
    else:
        return bin(s)[2:]