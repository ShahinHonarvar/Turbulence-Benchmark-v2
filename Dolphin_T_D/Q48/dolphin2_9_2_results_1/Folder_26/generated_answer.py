def return_binary_or_hexa(nums):
    a = nums[68]
    b = nums[99]
    s = sum(set(range(a + 1, b)) - set(nums[68:100]))
    if s % 2:
        return str(bin(s))[2:]
    else:
        return str(hex(s))[2:].upper() if s != 0 else ''