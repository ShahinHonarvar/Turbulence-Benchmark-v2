def return_binary_or_hexa(t):
    a = t[3]
    b = t[9]
    missing = []
    for i in range(a + 1, b):
        if i not in t[4:9]:
            missing.append(i)
    total = sum(missing)
    if total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]