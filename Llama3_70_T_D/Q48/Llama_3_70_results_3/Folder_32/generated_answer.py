def return_binary_or_hexa(nums):
    a, b = (nums[86], nums[90])
    total = sum((i for i in range(a + 1, b) if i not in nums[86:91]))
    if not total:
        return ''
    return bin(total)[2:] if total % 2 else hex(total)[2:]