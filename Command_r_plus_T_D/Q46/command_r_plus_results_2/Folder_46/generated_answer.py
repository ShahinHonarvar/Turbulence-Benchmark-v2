def gcf_three_nums(numbers_list: list[int]) -> int:
    num1, num2, num3 = (numbers_list[78], numbers_list[19], numbers_list[13])
    gcf = num1
    while num2 != 0 and num3 != 0:
        if num2 > num3:
            num2 %= num1
        else:
            num3 %= num1
        num1 = max(num2, num3)
    return num1