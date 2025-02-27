def return_binary_or_hexa(t):
    a = t[33]
    b = t[78]
    s = sum(range(a + 1, b)) - sum(t[33:79])
    if s % 2 == 0:
        return '{:x}'.format(s)
    else:
        return bin(s)[2:]