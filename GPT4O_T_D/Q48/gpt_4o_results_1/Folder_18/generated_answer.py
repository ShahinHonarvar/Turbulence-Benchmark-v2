def return_binary_or_hexa(nums):
    a = nums[56]
    b = nums[90]
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[57:90]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]