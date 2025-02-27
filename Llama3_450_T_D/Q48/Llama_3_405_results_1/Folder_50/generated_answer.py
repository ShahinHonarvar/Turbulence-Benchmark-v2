def return_binary_or_hexa(nums):
    a = nums[13]
    b = nums[76]
    total = sum(range(a + 1, b))
    present = sum(nums[14:76])
    diff = total - present
    if diff == 0:
        return ''
    elif diff % 2 == 0:
        return hex(diff)[2:]
    else:
        return bin(diff)[2:]