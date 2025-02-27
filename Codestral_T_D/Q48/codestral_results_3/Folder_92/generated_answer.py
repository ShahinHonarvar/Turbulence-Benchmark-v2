def return_binary_or_hexa(t):
    a = t[0]
    b = t[2]
    missing_nums_sum = sum((x for x in range(a + 1, b) if x not in t))
    if missing_nums_sum % 2 == 1:
        return bin(missing_nums_sum)[2:]
    elif missing_nums_sum > 0:
        return hex(missing_nums_sum)[2:]
    else:
        return ''