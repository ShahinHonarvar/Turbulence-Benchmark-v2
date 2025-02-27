def return_binary_or_hexa(nums):
    a = nums[38]
    b = nums[81]
    total = sum((i for i in range(a + 1, b) if i not in nums[38:82]))
    return bin(total)[2:] if total % 2 != 0 else hex(total)[2:]