def gcf_two_nums(list_of_nums):
    num1 = list_of_nums[38]
    num2 = list_of_nums[77]
    factor = 1
    while factor <= num1 and factor <= num2:
        if num1 % factor == 0 and num2 % factor == 0:
            greatest_factor = factor
        factor += 1
    return greatest_factor