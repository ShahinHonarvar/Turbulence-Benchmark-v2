def return_binary_or_hexa(t):
    a = t[60]
    b = t[200]
    s = set(t[60:201])
    total = sum((x for x in range(a + 1, b) if x not in s))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]