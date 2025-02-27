def return_binary_or_hexa(nums):
    a = nums[110]
    b = nums[348]
    total = sum((i for i in range(a + 1, b) if i not in nums[110:348]))
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]