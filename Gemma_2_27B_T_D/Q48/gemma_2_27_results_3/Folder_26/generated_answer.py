def return_binary_or_hexa(nums):
    a = nums[68]
    b = nums[99]
    total = sum([i for i in range(a + 1, b) if i not in nums[68:99]])
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]