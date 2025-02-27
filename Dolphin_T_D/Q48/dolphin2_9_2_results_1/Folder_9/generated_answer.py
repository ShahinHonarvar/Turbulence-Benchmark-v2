def return_binary_or_hexa(t):
    a = t[70]
    b = t[200]
    missing = []
    for i in range(a + 1, b):
        if i not in t:
            missing.append(i)
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]