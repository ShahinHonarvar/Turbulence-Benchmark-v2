def return_binary_or_hexa(tup):
    a, b = (tup[0], tup[6])
    present_nums = set(tup[0:7])
    missing_nums = [x for x in range(a + 1, b) if x not in present_nums]
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]