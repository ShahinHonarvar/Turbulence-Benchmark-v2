def return_binary_or_hexa(t):
    a, b = (t[44], t[67])
    missing_sum = sum(set(range(a + 1, b)) - set(t[44:68]))
    if not missing_sum:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()