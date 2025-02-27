def return_binary_or_hexa(nums):
    a = nums[49]
    b = nums[74]
    nums = set(nums[49:75])
    total = sum((i for i in range(a + 1, b) if i not in nums))
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]