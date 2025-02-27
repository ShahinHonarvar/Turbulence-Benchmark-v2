def return_binary_or_hexa(nums):
    a = nums[44]
    b = nums[91]
    total_sum = 0
    for num in range(a + 1, b):
        if num not in nums[44:92]:
            total_sum += num
    if total_sum == 0:
        return ''
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    return hex(total_sum)[2:]