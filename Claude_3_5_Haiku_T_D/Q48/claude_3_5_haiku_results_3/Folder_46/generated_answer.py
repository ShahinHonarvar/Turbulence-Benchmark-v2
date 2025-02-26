def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[79]
    missing_nums = set(range(a + 1, b)) - set(nums[10:80])
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]