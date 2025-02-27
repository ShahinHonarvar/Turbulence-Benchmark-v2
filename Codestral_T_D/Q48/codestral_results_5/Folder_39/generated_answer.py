def return_binary_or_hexa(nums):
    a = nums[44]
    b = nums[91]
    missing_nums = set(range(a + 1, b))
    present_nums = set(nums[44 + 1:91])
    missing_sum = sum(missing_nums - present_nums)
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]