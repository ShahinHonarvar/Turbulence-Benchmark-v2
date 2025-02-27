def return_binary_or_hexa(t):
    a = t[40]
    b = t[200]
    if all((i in t for i in range(a + 1, b))):
        return ''
    missing_sum = sum((i for i in range(a + 1, b) if i not in t))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]