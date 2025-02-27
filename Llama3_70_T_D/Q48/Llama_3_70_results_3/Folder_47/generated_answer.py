def return_binary_or_hexa(nums):
    a = nums[29]
    b = nums[53]
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[29:54]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]