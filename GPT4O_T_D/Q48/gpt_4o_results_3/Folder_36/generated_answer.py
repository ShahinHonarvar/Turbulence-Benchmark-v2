def return_binary_or_hexa(nums):
    a = nums[110]
    b = nums[348]
    required_nums = set(range(a + 1, b))
    present_nums = set(nums[111:348])
    missing_nums = required_nums - present_nums
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]