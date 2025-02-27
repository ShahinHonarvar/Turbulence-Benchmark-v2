def return_binary_or_hexa(t):
    a = t[57]
    b = t[85]
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[57:85]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]