def return_binary_or_hexa(t):
    a = t[20]
    b = t[51]
    s = 0
    present = [False] * (b - a + 1)
    for i in t[20:52]:
        if a < i <= b:
            present[i - a] = True
    for i in range(1, len(present)):
        if not present[i]:
            s += a + i
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()