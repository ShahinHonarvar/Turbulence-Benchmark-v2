def return_binary_or_hexa(tup):
    a = tup[2]
    b = tup[7]
    missing_nums = [num for num in range(a + 1, b) if num not in tup[2:8]]
    if not missing_nums:
        return ''
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]