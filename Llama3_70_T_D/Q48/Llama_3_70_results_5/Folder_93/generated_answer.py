def return_binary_or_hexa(nums):
    a = nums[57]
    b = nums[85]
    nums_set = set(nums[57:86])
    total_sum = sum((i for i in range(a + 1, b) if i not in nums_set))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    elif total_sum == 0:
        return ''
    else:
        return hex(total_sum)[2:]