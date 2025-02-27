def return_binary_or_hexa(nums):
    a, b = (nums[72], nums[93])
    missing_nums = [i for i in range(a + 1, b) if i not in nums[72:93]]
    total = sum(missing_nums)
    if total:
        return bin(total)[2:] if total % 2 else hex(total)[2:]
    return ''