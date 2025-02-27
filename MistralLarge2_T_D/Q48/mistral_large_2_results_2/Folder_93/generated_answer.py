def return_binary_or_hexa(t):
    a = t[57]
    b = t[85]
    range_set = set(range(a + 1, b))
    present_set = set(t[57:86])
    missing_sum = sum(range_set - present_set)
    if not missing_sum:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()