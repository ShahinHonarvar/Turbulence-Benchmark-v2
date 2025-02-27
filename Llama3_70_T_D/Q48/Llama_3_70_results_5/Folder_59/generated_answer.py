def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[10]
    full_set = set(range(a + 1, b))
    num_set = set(nums[1:10])
    missing_nums = full_set - num_set
    total = sum(missing_nums)
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]