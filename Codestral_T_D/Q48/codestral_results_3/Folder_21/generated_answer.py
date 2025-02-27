def return_binary_or_hexa(nums):
    a, b = (nums[15], nums[57])
    missing = set(range(a + 1, b)) - set(nums[16:57])
    total = sum(missing)
    return bin(total)[2:] if total % 2 else hex(total)[2:]