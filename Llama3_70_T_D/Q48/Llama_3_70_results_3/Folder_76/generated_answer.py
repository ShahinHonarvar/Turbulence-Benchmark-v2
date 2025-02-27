def return_binary_or_hexa(nums):
    a = nums[450]
    b = nums[905]
    total_sum = sum((i for i in range(a + 1, b) if i not in nums[450:906]))
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]