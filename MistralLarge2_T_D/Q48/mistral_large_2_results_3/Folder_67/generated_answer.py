def return_binary_or_hexa(t):
    a = t[44]
    b = t[67]
    missing_sum = sum(set(range(a + 1, b)) - set(t[44:68]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:].upper()