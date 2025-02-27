def return_binary_or_hexa(t):
    a = t[427]
    b = t[669]
    missing = sum()
    for i in range(a + 1, b):
        if i not in t:
            missing += i
    if missing % 2:
        return bin(missing)[2:]
    else:
        return hex(missing)[2:].upper()