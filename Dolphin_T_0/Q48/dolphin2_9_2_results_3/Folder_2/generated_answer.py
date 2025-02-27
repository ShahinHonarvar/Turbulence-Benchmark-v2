def return_binary_or_hexa(t):
    a = t[72]
    b = t[93]
    missing = []
    for x in range(a + 1, b):
        if x not in t[72:94]:
            missing.append(x)
    result = sum(missing)
    if result % 2 == 0:
        return hexa(result)
    else:
        return bin(result)[2:]

def hexa(n):
    return hex(n)[2:]