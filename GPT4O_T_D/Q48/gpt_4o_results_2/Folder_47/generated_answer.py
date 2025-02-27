def return_binary_or_hexa(nums):
    a = nums[29]
    b = nums[53]
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[30:54]))
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]