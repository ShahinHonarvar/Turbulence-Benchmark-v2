def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[36]
    missing_nums = set(range(a + 1, b)) - set(nums[21:36])
    total = sum(missing_nums)
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]