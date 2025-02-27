def return_binary_or_hexa(nums):
    a = nums[11]
    b = nums[76]
    included = [num for num in nums if num >= a and num <= b]
    if all((num in included for num in range(a + 1, b))):
        return ''
    else:
        s = sum((num for num in range(a + 1, b) if num not in included))
        if s % 2 == 1:
            return bin(s)[2:]
        else:
            return hex(s)[2:]