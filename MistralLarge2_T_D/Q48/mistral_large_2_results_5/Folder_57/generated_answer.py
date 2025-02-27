def return_binary_or_hexa(tup):
    a = tup[25]
    b = tup[80]
    sub_tup = tup[25:81]
    missing_sum = sum((x for x in range(a + 1, b) if x not in sub_tup))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]