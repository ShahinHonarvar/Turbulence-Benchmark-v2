def return_binary_or_hexa(nums):
    a, b = (nums[13], nums[70])
    total = sum((i for i in range(a + 1, b) if i not in nums[13:71]))
    return bin(total)[2:] if total % 2 else hex(total)[2:].upper()