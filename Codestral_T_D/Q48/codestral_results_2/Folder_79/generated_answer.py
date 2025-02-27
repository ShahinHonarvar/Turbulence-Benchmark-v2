def return_binary_or_hexa(tup):
    a, b = (tup[1], tup[7])
    missing_sum = sum(range(a + 1, b)) - sum(tup[2:7])
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]