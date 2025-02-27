def return_binary_or_hexa(t):
    a = t[34]
    b = t[69]
    missing_sum = sum(set(range(a + 1, b)) - set(t[34:70]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]