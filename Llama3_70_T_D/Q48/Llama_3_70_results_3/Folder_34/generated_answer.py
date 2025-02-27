def return_binary_or_hexa(nums):
    a = nums[60]
    b = nums[200]
    total_sum = sum((i for i in range(a + 1, b) if i not in nums[61:200]))
    if total_sum == 0:
        return ''
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    return hex(total_sum)[2:]