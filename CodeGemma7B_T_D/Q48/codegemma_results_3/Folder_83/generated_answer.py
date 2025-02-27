def return_binary_or_hexa(nums):
    total = sum((n for n in range(nums[90] + 1, nums[200] + 1) if n not in nums))
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()