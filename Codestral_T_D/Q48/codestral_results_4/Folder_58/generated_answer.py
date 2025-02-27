def return_binary_or_hexa(nums):
    a, b = (nums[275], nums[871])
    missing = set(range(a + 1, b)) - set(nums[275 + 1:871])
    s = sum(missing)
    return bin(s)[2:] if s % 2 else hex(s)[2:]