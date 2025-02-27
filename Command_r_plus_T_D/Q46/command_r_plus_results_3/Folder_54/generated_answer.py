def gcf_three_nums(numbers_list: list[int]) -> int:
    num1, num2, num3 = (numbers_list[96], numbers_list[57], numbers_list[85])
    gcf = num1
    while num2 != 0 and num3 != 0:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
        if num1 > num3:
            num1 = num1 - num3
        else:
            num3 = num3 - num1
    gcf = num1
    return gcf