def gcf_three_nums(numbers_list: list[int]) -> int:
    num1, num2, num3 = (numbers_list[78], numbers_list[19], numbers_list[13])
    gcf = num1
    while num2 != 0 and num3 != 0:
        if num2 > num3:
            num2 %= num3
        else:
            num3 %= num2
        if gcf % num2 == 0 and gcf % num3 == 0:
            gcf = num2 + num3
        else:
            gcf = num2 if num2 > num3 else num3
    return gcf