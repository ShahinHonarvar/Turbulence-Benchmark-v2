def return_binary_or_hexa(nums):
    nums, a, b = (nums[:56], nums[56], nums[88])
    c = 0
    for x in range(a + 1, b):
        if x not in nums and x not in range(a + 1, b):
            c += x
    return bin(c)[2:] if c % 2 else hex(c)[2:].upper()