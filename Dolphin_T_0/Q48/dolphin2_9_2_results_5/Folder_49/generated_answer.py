def return_binary_or_hexa(nums):
    a = nums[80]
    b = nums[200]
    if a == b:
        return ''
    s = 0
    for i in range(a + 1, b):
        if i not in nums:
            s += i
    if s % 2 == 0:
        return hex(s)[2:].upper()
    else:
        return bin(s)[2:]