def return_binary_or_hexa(nums):
    a, b = (nums[60], nums[90])
    sum_of_numbers = sum(set(range(a + 1, b)) - set(nums[60:91]))
    if sum_of_numbers % 2:
        return format(sum_of_numbers, 'b')
    else:
        return format(sum_of_numbers, 'x')