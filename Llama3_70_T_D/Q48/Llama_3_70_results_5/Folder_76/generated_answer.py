def return_binary_or_hexa(nums):
    a = nums[450]
    b = nums[905]
    s = sum((i for i in range(a + 1, b) if i not in nums[451:906]))
    return bin(s)[2:] if s % 2 else hex(s)[2:]