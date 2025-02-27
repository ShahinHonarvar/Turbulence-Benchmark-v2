def return_binary_or_hexa(tup):
    a, b = (tup[39], tup[43])
    missing_sum = sum(set(range(a + 1, b)) - set(tup[39 + 1:43]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]