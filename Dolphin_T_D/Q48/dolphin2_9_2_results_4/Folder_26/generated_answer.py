def return_binary_or_hexa(t):
    a = t[68]
    b = t[99]
    s = sum(set(range(a + 1, b)) - set(t[69:99]))
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]