def return_binary_or_hexa(t):
    a, b = (t[0], t[4])
    if all((a + 1 <= i <= b - 1 for i in t[1:4])):
        return ''
    s = sum((i for i in range(a + 1, b) if i not in t[1:4]))
    if s % 2 != 0:
        return bin(s)[2:]
    else:
        return hex(s)[2:]