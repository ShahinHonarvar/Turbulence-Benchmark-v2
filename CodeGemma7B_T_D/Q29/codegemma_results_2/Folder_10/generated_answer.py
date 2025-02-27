def gcf_two_nums(list_of_nums):
    num1 = list_of_nums[15]
    num2 = list_of_nums[99]
    min_num = min(num1, num2)
    for i in range(min_num, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i