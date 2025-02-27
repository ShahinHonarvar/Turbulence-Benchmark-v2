def return_binary_or_hexa(nums):
    a = nums[45]
    b = nums[48]
    missing_nums = set(range(a + 1, b))
    present_nums = set(nums[45 + 1:48])
    missing_sum = sum(missing_nums - present_nums)
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]