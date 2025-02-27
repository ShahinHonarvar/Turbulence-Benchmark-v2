def return_binary_or_hexa(nums):
    a = nums[56]
    b = nums[90]
    present = set(nums[56:91])
    total = sum((i for i in range(a + 1, b) if i not in present))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]