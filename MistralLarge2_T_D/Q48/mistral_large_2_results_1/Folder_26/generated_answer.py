def return_binary_or_hexa(nums):
    a, b = (nums[68], nums[99])
    sub_nums = set(nums[68:100])
    missing_sum = sum((x for x in range(a + 1, b) if x not in sub_nums))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]