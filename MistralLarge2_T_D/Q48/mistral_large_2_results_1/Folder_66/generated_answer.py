def return_binary_or_hexa(nums):
    a, b = (nums[11], nums[76])
    sum_missing = sum(set(range(a + 1, b)) - set(nums[11:77]))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()