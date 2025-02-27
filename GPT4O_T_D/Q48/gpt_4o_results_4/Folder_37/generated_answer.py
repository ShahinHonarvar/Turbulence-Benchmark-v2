def return_binary_or_hexa(nums):
    a, b = (nums[2], nums[7])
    present_nums = set(nums[3:7])
    sum_missing = sum((x for x in range(a + 1, b) if x not in present_nums))
    if sum_missing == 0:
        return ''
    return bin(sum_missing)[2:] if sum_missing % 2 else hex(sum_missing)[2:]