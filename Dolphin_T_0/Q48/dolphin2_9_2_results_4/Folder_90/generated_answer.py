def return_binary_or_hexa(nums):
    a = nums[60]
    b = nums[90]
    s = sum(nums[61:90])
    if all((num in nums for num in range(a + 1, b))):
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()