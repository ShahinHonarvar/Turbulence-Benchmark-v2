def return_binary_or_hexa(nums):
    a = nums[86]
    b = nums[90]
    total = sum(range(a + 1, b))
    present = sum(nums[87:90])
    diff = total - present
    if diff == 0:
        return ''
    elif diff % 2 == 0:
        return hex(diff)[2:]
    else:
        return bin(diff)[2:]