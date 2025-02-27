def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[12]
    total = sum((i for i in range(a + 1, b) if i not in nums[10:12]))
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()