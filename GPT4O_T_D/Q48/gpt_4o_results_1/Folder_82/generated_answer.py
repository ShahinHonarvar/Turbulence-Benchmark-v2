def return_binary_or_hexa(t):
    if len(t) < 201:
        return ''
    a = t[20]
    b = t[200]
    missing_sum = sum((x for x in range(a + 1, b) if x not in t[21:200]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]