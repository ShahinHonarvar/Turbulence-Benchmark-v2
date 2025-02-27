def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[6]
    total = sum((i for i in range(a + 1, b) if i not in nums))
    if total == 0:
        return ''
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]