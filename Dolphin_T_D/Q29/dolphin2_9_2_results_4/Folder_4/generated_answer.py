def gcf_two_nums(nums_list):
    num1 = nums_list[76]
    num2 = nums_list[57]
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1
    for i in range(1, smaller + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
    return gcf