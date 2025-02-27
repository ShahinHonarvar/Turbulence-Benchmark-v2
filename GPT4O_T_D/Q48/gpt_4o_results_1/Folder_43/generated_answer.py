def return_binary_or_hexa(t):
    if len(t) < 29:
        return ''
    a = t[10]
    b = t[28]
    if a >= b - 1:
        return ''
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[11:29]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]