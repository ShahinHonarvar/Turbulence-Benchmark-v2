def return_binary_or_hexa(t):
    a = t[1]
    b = t[8]
    present_nums = set(t)
    nums = set(range(a + 1, b))
    missing_nums = nums.difference(present_nums)
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]