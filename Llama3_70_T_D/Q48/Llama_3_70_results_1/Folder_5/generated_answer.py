def return_binary_or_hexa(nums):
    a = nums[2]
    b = nums[8]
    full_set = set(range(a + 1, b))
    nums_set = set(nums[2:9])
    missing_nums = full_set - nums_set
    total_sum = sum(missing_nums)
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]