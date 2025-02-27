def return_binary_or_hexa(t):
    a = t[57]
    b = t[84]
    missing_sum = sum((i for i in range(a + 1, b) if t[57:85].count(i) == 0))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()