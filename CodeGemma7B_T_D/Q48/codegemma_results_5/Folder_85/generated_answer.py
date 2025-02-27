def return_binary_or_hexa(t):
    a, b = (t[1], t[8])
    if a + 1 == b and t[1] in range(1, 9):
        return ''
    s = 0
    for x in range(a + 1, b):
        if x not in t[1:8]:
            s += x
    return bin(s)[2:].zfill(int(len(bin(s)) - 2)) if s % 2 == 1 else hex(s)[2:].zfill(int(len(hex(s)) - 2))