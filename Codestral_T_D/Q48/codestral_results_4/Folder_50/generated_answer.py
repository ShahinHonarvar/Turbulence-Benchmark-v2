def return_binary_or_hexa(t):
    a = t[13]
    b = t[76]
    missing_nums_sum = sum((i for i in range(a + 1, b) if i not in t[13:77]))
    if missing_nums_sum == 0:
        return ''
    elif missing_nums_sum % 2 == 1:
        return bin(missing_nums_sum)[2:]
    else:
        return hex(missing_nums_sum)[2:]