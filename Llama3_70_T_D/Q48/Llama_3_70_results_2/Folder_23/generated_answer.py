def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[36]
    total_sum = sum((i for i in range(a + 1, b) if i not in nums[20:37]))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    elif total_sum:
        return hex(total_sum)[2:]
    else:
        return ''