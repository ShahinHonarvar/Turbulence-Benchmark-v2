def return_binary_or_hexa(nums):
    a, b = (nums[80], nums[200])
    total_sum = sum((i for i in range(a + 1, b) if i not in nums[80:201]))
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]