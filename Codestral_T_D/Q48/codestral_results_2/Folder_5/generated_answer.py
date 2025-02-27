def return_binary_or_hexa(t):
    a, b = (t[2], t[8])
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[2:8]))
    if not missing_sum:
        return ''
    elif missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]