def return_binary_or_hexa(t):
    if len(t) < 77:
        return ''
    a = t[11]
    b = t[76]
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[12:77]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]