def return_binary_or_hexa(nums):
    a, b = (nums[90], nums[200])
    present = set(nums[90:201])
    total = sum((i for i in range(a + 1, b) if i not in present))
    if total == 0:
        return ''
    return bin(total)[2:] if total % 2 else hex(total)[2:].upper()