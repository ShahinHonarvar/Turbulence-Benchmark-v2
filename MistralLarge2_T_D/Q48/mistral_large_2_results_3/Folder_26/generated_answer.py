def return_binary_or_hexa(t):
    a = t[68]
    b = t[99]
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[68:100]))
    if not missing_sum:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()