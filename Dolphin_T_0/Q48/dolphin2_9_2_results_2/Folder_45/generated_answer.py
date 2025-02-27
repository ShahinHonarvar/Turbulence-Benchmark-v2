def return_binary_or_hexa(t):
    a = t[30]
    b = t[200]
    s = 0
    for i in range(a + 1, b):
        if i not in t[30:200]:
            s += i
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]