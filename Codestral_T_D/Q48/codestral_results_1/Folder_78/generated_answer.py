def return_binary_or_hexa(nums):
    a = nums[62]
    b = nums[96]
    nums_range = set(nums[62:96])
    missing_nums = set(range(a + 1, b))
    if missing_nums.issubset(nums_range):
        return ''
    else:
        missing_sum = sum(missing_nums - nums_range)
        if missing_sum % 2 == 1:
            return bin(missing_sum)[2:]
        else:
            return hex(missing_sum)[2:]