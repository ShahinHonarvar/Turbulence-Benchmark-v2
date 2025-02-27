def return_binary_or_hexa(t):
    a = t[86]
    b = t[99]
    s = sum(range(a + 1, b)) - sum(t[87:99])
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]