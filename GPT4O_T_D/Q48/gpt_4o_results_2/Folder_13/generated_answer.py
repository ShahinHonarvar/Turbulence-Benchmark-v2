def return_binary_or_hexa(nums):
    a = nums[46]
    b = nums[91]
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[46:92]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:]