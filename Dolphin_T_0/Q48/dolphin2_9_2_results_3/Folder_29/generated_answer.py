def return_binary_or_hexa(nums):
    a = nums[70]
    b = nums[98]
    present = set(nums[70:99])
    total = sum(set(range(a + 1, b)) - present)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()