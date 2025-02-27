def return_binary_or_hexa(t):
    a = t[427]
    b = t[669]
    s = sum(set(range(a + 1, b)) - set(t[427:670]))
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]