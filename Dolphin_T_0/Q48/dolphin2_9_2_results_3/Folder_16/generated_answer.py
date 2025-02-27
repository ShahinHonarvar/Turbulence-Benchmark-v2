def return_binary_or_hexa(t):
    a = t[90]
    b = t[97]
    missing = []
    for i in range(a + 1, b):
        if i not in t[90:97]:
            missing.append(i)
    total = sum(missing)
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]