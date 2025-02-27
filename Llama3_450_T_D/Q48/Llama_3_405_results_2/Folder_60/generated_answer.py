def return_binary_or_hexa(nums):
    a = nums[38]
    b = nums[52]
    total = sum(range(a + 1, b))
    present = sum(nums[39:52])
    diff = total - present
    if diff == 0:
        return ''
    elif diff % 2 == 1:
        return bin(diff)[2:]
    else:
        return hex(diff)[2:]