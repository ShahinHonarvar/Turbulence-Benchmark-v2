def return_binary_or_hexa(nums):
    a, b = (nums[50], nums[200])
    s = sum((i for i in range(a + 1, b) if i not in nums[50:201]))
    return bin(s)[2:] if s % 2 else hex(s)[2:]