def return_binary_or_hexa(nums):
    a = nums[13]
    b = nums[76]
    excluded = set(nums[13:77])
    total = sum((num for num in range(a + 1, b) if num not in excluded))
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]