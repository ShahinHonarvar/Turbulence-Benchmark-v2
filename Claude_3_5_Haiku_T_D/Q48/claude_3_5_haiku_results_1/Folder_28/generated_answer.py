def return_binary_or_hexa(tup):
    a = tup[86]
    b = tup[99]
    missing_nums = []
    for num in range(a + 1, b):
        if num not in tup[86:100]:
            missing_nums.append(num)
    if not missing_nums:
        return ''
    sum_missing = sum(missing_nums)
    if sum_missing % 2:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]