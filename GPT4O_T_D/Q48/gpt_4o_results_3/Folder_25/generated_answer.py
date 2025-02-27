def return_binary_or_hexa(t):
    a = t[37]
    b = t[43]
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[38:43]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]