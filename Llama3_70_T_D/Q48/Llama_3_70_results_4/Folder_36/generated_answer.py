def return_binary_or_hexa(nums):
    a = nums[110]
    b = nums[348]
    present_nums = set(nums[110:349])
    sum_val = sum((i for i in range(a + 1, b) if i not in present_nums))
    if sum_val == 0:
        return ''
    elif sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:]