def gcf_two_nums(list_of_nums):
    num1 = list_of_nums[37]
    num2 = list_of_nums[30]
    common_factor = 1
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            common_factor = i
    return common_factor