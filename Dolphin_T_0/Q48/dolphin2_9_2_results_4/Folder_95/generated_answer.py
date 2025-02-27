def return_binary_or_hexa(tup):
    a = tup[32]
    b = tup[99]
    missing_nums = [x for x in range(a + 1, b) if x not in tup]
    if missing_nums:
        sum_of_missing = sum(missing_nums)
        if sum_of_missing % 2 == 0:
            return hex(sum_of_missing)[2:]
        else:
            return bin(sum_of_missing)[2:]
    else:
        return ''