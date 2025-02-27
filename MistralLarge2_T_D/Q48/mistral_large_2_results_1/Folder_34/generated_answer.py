def return_binary_or_hexa(nums):
    a, b = (nums[60], nums[200])
    num_set = set(nums[60:201])
    missing_sum = sum((x for x in range(a + 1, b) if x not in num_set))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]