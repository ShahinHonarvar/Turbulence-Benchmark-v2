def return_binary_or_hexa(nums):
    a = nums[32]
    b = nums[99]
    missing = set(range(a + 1, b)) - set(nums[32:99])
    total = sum(missing)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]