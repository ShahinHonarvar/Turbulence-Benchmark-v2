def gcf_three_nums(num_list):
    num1 = num_list[16]
    num2 = num_list[87]
    num3 = num_list[95]
    if num1 < num2:
        num1, num2 = (num2, num1)
    if num1 < num3:
        num1, num3 = (num3, num1)
    while num2 != 0 and num3 != 0:
        if num2 > num3:
            num2 %= num3
        else:
            num3 %= num2
    return num1 // (num2 + num3)