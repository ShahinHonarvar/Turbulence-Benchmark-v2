def return_binary_or_hexa(t):
    a, b = (t[18], t[52])
    missing_sum = sum((x for x in range(a + 1, b) if x not in t[18:53]))
    if not missing_sum:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()