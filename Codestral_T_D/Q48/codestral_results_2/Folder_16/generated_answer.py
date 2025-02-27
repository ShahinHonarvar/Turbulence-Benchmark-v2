def return_binary_or_hexa(tup):
    a = tup[90]
    b = tup[97]
    missing_nums_sum = sum((x for x in range(a + 1, b) if x not in tup[90:98]))
    if missing_nums_sum % 2 == 1:
        return bin(missing_nums_sum)[2:]
    else:
        return hex(missing_nums_sum)[2:]