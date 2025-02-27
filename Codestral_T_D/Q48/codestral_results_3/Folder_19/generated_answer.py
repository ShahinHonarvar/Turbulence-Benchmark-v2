def return_binary_or_hexa(tup):
    a = tup[1]
    b = tup[4]
    missing_nums = set(range(a + 1, b))
    present_nums = set(tup[1:4])
    missing_sum = sum(missing_nums - present_nums)
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()