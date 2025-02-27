def return_binary_or_hexa(t):
    a = t[427]
    b = t[669]
    if a + 1 > b - 1:
        return ''
    s = sum(set(range(a + 1, b)) - set(t[428:670]))
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]