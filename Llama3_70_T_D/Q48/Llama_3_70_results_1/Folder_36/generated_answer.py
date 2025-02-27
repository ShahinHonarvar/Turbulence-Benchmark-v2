def return_binary_or_hexa(nums):
    a = nums[110]
    b = nums[348]
    present_nums = set(nums[110:349])
    missing_nums_sum = sum((i for i in range(a + 1, b) if i not in present_nums))
    if missing_nums_sum == 0:
        return ''
    elif missing_nums_sum % 2 == 1:
        return bin(missing_nums_sum)[2:]
    else:
        return hex(missing_nums_sum)[2:]