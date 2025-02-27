def return_binary_or_hexa(nums):
    a = nums[3]
    b = nums[9]
    nums_set = set(nums[3:10])
    total_sum = sum((i for i in range(a + 1, b) if i not in nums_set))
    if total_sum == 0:
        return ''
    elif total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]