def return_binary_or_hexa(nums):
    a = nums[57]
    b = nums[85]
    existing_nums = set(nums[57:86])
    sum_value = sum((num for num in range(a + 1, b) if num not in existing_nums))
    if sum_value == 0:
        return ''
    elif sum_value % 2 == 1:
        return bin(sum_value)[2:]
    else:
        return hex(sum_value)[2:]