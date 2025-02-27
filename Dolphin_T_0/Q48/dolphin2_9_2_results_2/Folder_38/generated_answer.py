def return_binary_or_hexa(t):
    a = t[36]
    b = t[85]
    missing = []
    for i in range(a + 1, b):
        if i not in t:
            missing.append(i)
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]