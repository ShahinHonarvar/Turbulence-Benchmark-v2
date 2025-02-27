def return_binary_or_hexa(t):
    a = t[0]
    b = t[8]
    missing = [i for i in range(a + 1, b) if i not in t]
    result = sum(missing)
    if result % 2 == 1:
        return bin(result)[2:]
    else:
        return hex(result)[2:].upper()