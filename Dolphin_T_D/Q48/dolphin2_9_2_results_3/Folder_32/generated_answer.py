def return_binary_or_hexa(t):
    a = t[86]
    b = t[90]
    present = {x for x in t[87:90]}
    s = sum((x for x in range(a + 1, b) if x not in present))
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]