def return_binary_or_hexa(t):
    a = t[10]
    b = t[12]
    s = set(range(a + 1, b))
    missing_sum = sum(s - set(t[11:12]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]