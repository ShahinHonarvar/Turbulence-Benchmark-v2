def return_binary_or_hexa(nums):
    a = nums[32]
    b = nums[44]
    full_set = set(range(a + 1, b))
    num_set = set(nums[33:44])
    missing_nums = full_set - num_set
    total = sum(missing_nums)
    if total % 2 == 1:
        return bin(total)[2:]
    elif total == 0:
        return ''
    else:
        return hex(total)[2:]