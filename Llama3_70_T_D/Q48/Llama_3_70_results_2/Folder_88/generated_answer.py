def return_binary_or_hexa(nums):
    a = nums[3]
    b = nums[9]
    full_set = set(range(a + 1, b))
    subset = set(nums[4:10])
    missing_nums = full_set - subset
    total = sum(missing_nums)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]