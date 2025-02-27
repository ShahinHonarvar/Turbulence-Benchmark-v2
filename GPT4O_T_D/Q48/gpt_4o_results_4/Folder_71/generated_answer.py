def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[35]
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[21:36]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]