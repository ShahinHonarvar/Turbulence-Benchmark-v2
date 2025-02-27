def return_binary_or_hexa(t):
    a = t[450]
    b = t[905]
    missing_sum = sum((x for x in range(a + 1, b) if x not in t[450:906]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()