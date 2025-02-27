def return_binary_or_hexa(t):
    a = t[2]
    b = t[8]
    missing_nums_sum = sum(range(a + 1, b)) - sum(t[2:9])
    if missing_nums_sum == 0:
        return ''
    elif missing_nums_sum % 2 == 1:
        return bin(missing_nums_sum)[2:]
    else:
        return hex(missing_nums_sum)[2:]