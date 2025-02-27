def return_binary_or_hexa(t):
    a = t[38]
    b = t[52]
    missing_sum = sum(set(range(a + 1, b)) - set(t[38:53]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    elif missing_sum == 0:
        return ''
    else:
        return hex(missing_sum)[2:]