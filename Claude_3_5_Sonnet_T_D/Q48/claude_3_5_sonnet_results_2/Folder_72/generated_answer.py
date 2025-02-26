def return_binary_or_hexa(nums):
    a = nums[13]
    b = nums[70]
    range_set = set(nums[13:71])
    sum_value = sum((num for num in range(a + 1, b) if num not in range_set))
    if sum_value == 0:
        return ''
    elif sum_value % 2 == 1:
        return bin(sum_value)[2:]
    else:
        return hex(sum_value)[2:]