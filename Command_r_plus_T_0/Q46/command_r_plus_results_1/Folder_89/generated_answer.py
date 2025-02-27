def gcf_three_nums(numbers_list: list[int]) -> int:
    num1, num2, num3 = (numbers_list[63], numbers_list[73], numbers_list[11])
    gcf = num1
    while num2 != 0 and num3 != 0:
        if num2 > num3:
            num2 %= num1
        else:
            num3 %= num1
        gcf = num1
    return gcf