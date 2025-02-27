def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[36]
    nums_set = set(nums[20:37])
    total_sum = sum((i for i in range(a + 1, b) if i not in nums_set))
    if total_sum == 0:
        return ''
    elif total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]