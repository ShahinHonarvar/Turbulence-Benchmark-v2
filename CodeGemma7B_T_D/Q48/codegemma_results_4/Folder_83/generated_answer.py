def return_binary_or_hexa(nums):
    nums = sorted(set(nums))
    a, b = (nums[90], nums[200])
    result = sum((n for n in range(a + 1, b) if n not in nums))
    return bin(result)[2:] if result % 2 else hex(result)[2:].upper()