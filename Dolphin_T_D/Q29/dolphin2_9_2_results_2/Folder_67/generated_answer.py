def gcf_two_nums(nums_list):
    num1 = nums_list[64]
    num2 = nums_list[28]
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
    return gcf