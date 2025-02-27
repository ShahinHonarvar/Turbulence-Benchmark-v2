def return_binary_or_hexa(nums):
    a, b = (nums[11], nums[76])
    s = sum((i for i in range(a + 1, b) if i not in nums[11:77]))
    return bin(s)[2:] if s % 2 else hex(s)[2:].upper()