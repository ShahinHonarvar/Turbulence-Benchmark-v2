def return_binary_or_hexa(t):
    a = t[70]
    b = t[200]
    missing_sum = sum(set(range(a + 1, b)) - set(t[70:201]))
    if not missing_sum:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()