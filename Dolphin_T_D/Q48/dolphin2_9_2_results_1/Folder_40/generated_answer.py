def return_binary_or_hexa(t):
    a = t[0]
    b = t[3]
    present = set(t[1:4])
    s = sum((i for i in range(a + 1, b) if i not in present))
    return format(s, 'b') if s % 2 != 0 else hex(s)[2:]