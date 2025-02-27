def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[5]
    total = sum((i for i in range(a + 1, b) if i not in nums[:6]))
    if not total:
        return ''
    if total % 2:
        return bin(total)[2:]
    return hex(total)[2:]