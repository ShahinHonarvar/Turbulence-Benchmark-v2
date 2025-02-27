def return_binary_or_hexa(t):
    a, b = (t[50], t[200])
    present = set(t[50:201])
    s = sum((i for i in range(a + 1, b) if i not in present))
    if s == 0:
        return ''
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]