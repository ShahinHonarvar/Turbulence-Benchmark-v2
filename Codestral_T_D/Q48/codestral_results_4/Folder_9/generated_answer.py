def return_binary_or_hexa(nums):
    a, b = (nums[70], nums[200])
    s = sum(set(range(a + 1, b)) - set(nums[70 + 1:200]))
    return bin(s)[2:] if s % 2 else hex(s)[2:] if s else ''