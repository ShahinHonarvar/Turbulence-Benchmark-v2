def return_binary_or_hexa(t):
    a = t[34]
    b = t[69]
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[35:69]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]