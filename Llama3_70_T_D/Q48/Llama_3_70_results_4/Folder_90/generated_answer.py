def return_binary_or_hexa(nums):
    a = nums[60]
    b = nums[90]
    missing_nums = [i for i in range(a + 1, b) if i not in nums[61:90]]
    total_sum = sum(missing_nums)
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    elif total_sum != 0:
        return hex(total_sum)[2:]
    else:
        return ''