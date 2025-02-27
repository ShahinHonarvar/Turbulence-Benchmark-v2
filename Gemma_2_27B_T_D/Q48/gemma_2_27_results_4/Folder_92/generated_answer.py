def return_binary_or_hexa(nums):
    a, _, b = nums
    total = sum((i for i in range(a + 1, b) if i not in nums[0:3]))
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]