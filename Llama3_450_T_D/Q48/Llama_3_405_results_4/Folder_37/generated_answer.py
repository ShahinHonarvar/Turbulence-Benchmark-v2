def return_binary_or_hexa(t):
    a = t[2]
    b = t[7]
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[2:7]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]