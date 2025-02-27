def return_binary_or_hexa(t):
    a = t[17]
    b = t[88]
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[17:88]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]