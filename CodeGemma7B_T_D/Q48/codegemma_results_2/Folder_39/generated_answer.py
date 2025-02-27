def return_binary_or_hexa(nums):
    a, b = (nums[44], nums[91])
    total = sum((x for x in range(a + 1, b) if x not in nums[44:92]))
    return bin(total)[2:] if total % 2 else hex(total)[2:].upper() if all((x in nums[44:92] for x in range(a + 1, b))) else ''