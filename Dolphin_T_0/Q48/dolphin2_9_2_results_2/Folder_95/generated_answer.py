def return_binary_or_hexa(t):
    a = t[32]
    b = t[99]
    n = [i for i in range(a + 1, b) if i not in t[33:99]]
    if len(n) == 0:
        return ''
    s = sum(n)
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]