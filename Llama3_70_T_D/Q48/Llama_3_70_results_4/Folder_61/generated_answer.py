def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[8]
    total = sum((i for i in range(a + 1, b) if i not in nums[:9]))
    if total == 0:
        return ''
    if total % 2 == 1:
        return bin(total)[2:]
    return hex(total)[2:]