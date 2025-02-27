def return_binary_or_hexa(nums):
    a = nums[1]
    b = nums[7]
    total = sum((i for i in range(a + 1, b) if i not in nums[1:8]))
    if total == 0:
        return ''
    if total % 2 != 0:
        return bin(total)[2:]
    return hex(total)[2:]