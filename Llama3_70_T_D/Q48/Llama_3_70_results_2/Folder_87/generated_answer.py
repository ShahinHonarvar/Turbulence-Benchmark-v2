def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[43]
    total_sum = sum((i for i in range(a + 1, b) if i not in nums[20:44]))
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    elif total_sum == 0:
        return ''
    else:
        return hex(total_sum)[2:]