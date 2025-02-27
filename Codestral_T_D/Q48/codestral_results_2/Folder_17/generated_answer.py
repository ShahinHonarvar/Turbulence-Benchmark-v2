def return_binary_or_hexa(nums):
    a, b = (nums[73], nums[84])
    missing = set(range(a + 1, b)) - set(nums[73 + 1:84])
    total = sum(missing)
    if total % 2 == 1:
        return bin(total)[2:]
    elif total != 0:
        return hex(total)[2:]
    else:
        return ''