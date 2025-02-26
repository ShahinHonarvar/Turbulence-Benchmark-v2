def return_binary_or_hexa(tup):
    a = tup[38]
    b = tup[81]
    missing_nums = [num for num in range(a + 1, b) if num not in tup[38:82]]
    if not missing_nums:
        return ''
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]