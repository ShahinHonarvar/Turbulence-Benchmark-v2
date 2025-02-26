def return_binary_or_hexa(tup):
    a = tup[18]
    b = tup[60]
    missing_nums = set(range(a + 1, b)) - set(tup[18:61])
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]