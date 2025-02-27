def return_binary_or_hexa(t):
    a = t[32]
    b = t[44]
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[33:44]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]