def return_binary_or_hexa(t):
    a = t[18]
    b = t[52]
    missing_sum = sum(set(range(a + 1, b)) - set(t[18:53]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]