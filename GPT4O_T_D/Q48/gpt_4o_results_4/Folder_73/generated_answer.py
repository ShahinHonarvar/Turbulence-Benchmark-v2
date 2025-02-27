def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[76]
    nums_set = set(nums[11:76])
    total_sum = sum((x for x in range(a + 1, b) if x not in nums_set))
    if total_sum == 0:
        return ''
    if total_sum % 2:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]