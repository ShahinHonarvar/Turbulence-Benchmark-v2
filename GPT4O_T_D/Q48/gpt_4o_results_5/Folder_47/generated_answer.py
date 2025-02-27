def return_binary_or_hexa(nums):
    a = nums[29]
    b = nums[53]
    if b - a <= 1:
        return ''
    total_sum = sum((i for i in range(a + 1, b) if i not in nums[30:54]))
    if total_sum == 0:
        return ''
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]