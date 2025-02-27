def return_binary_or_hexa(nums):
    a = nums[77]
    b = nums[84]
    missing_nums = set(range(a + 1, b)) - set(nums[77:85])
    total_sum = sum(missing_nums)
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]