def return_binary_or_hexa(nums):
    a = nums[34]
    b = nums[69]
    total = sum((i for i in range(a + 1, b) if i not in nums[35:69]))
    if total == 0:
        return ''
    return bin(total)[2:] if total % 2 else hex(total)[2:]