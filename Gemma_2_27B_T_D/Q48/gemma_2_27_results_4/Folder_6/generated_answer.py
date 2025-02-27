def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[93]
    total = sum((x for x in range(a + 1, b) if x not in nums[20:94]))
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]