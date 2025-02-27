def return_binary_or_hexa(nums):
    a, b = (nums[43], nums[70])
    total = sum((i for i in range(a + 1, b) if i not in nums[44:71]))
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]