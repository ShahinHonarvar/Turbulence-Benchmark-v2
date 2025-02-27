def return_binary_or_hexa(t):
    a = t[30]
    b = t[200]
    present = set(range(a + 1, b))
    for i in t[31:200]:
        present.discard(i)
    s = sum(present)
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]