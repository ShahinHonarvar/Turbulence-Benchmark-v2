def return_binary_or_hexa(t):
    a = t[32]
    b = t[44]
    s = set(t[33:44])
    result = sum((i for i in range(a + 1, b) if i not in s))
    if result % 2 == 1:
        return bin(result)[2:]
    else:
        return hex(result)[2:].replace('b', '')