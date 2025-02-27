def return_binary_or_hexa(t):
    a = t[2]
    b = t[5]
    missing_nums_sum = sum((i for i in range(a + 1, b) if i not in t[2:5]))
    if missing_nums_sum % 2 == 1:
        return bin(missing_nums_sum)[2:]
    elif missing_nums_sum > 0:
        return hex(missing_nums_sum)[2:]
    else:
        return ''