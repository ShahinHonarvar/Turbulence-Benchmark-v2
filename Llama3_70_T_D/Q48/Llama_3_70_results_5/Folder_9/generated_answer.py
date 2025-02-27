def return_binary_or_hexa(nums):
    a = nums[70]
    b = nums[200]
    total = sum((i for i in range(a + 1, b) if i not in nums[71:201]))
    if total == 0:
        return ''
    if total % 2 == 0:
        return format(total, 'x')
    else:
        return bin(total)[2:]