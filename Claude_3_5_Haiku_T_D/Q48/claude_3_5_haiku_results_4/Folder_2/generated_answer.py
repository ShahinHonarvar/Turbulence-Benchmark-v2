def return_binary_or_hexa(nums):
    a = nums[72]
    b = nums[93]
    missing_nums_sum = 0
    for num in range(a + 1, b):
        if num not in nums[72:94]:
            missing_nums_sum += num
    if missing_nums_sum % 2 == 1:
        return bin(missing_nums_sum)[2:]
    elif missing_nums_sum > 0:
        return hex(missing_nums_sum)[2:]
    else:
        return ''