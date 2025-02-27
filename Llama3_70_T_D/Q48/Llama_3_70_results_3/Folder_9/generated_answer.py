def return_binary_or_hexa(nums):
    a, b = (nums[70], nums[200])
    total_sum = sum((i for i in range(a + 1, b) if i not in nums[71:201]))
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]