def return_binary_or_hexa(nums):
    a = nums[15]
    b = nums[57]
    missing_nums = [x for x in range(a + 1, b) if x not in nums[15:58]]
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]