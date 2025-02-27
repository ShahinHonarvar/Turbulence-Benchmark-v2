def return_binary_or_hexa(nums):
    a = nums[38]
    b = nums[52]
    missing_nums = set(range(a + 1, b))
    present_nums = set(nums[38 + 1:52])
    missing_sum = sum(missing_nums - present_nums)
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    elif missing_sum > 0:
        return hex(missing_sum)[2:]
    else:
        return ''