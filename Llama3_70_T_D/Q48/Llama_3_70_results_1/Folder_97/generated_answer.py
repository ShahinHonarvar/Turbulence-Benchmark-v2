def return_binary_or_hexa(nums):
    a = nums[34]
    b = nums[69]
    nums_set = set(nums[34:70])
    total_sum = sum((i for i in range(a + 1, b) if i not in nums_set))
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]