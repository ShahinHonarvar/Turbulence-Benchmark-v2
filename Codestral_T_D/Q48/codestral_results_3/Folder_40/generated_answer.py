def return_binary_or_hexa(tup):
    a, b = (tup[0], tup[3])
    missing_nums = set(range(a + 1, b)) - set(tup[1:3])
    missing_sum = sum(missing_nums)
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]