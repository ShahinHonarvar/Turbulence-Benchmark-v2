def return_binary_or_hexa(tup):
    a = tup[56]
    b = tup[88]
    missing_nums = [x for x in range(a + 1, b) if x not in tup[56:89]]
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]