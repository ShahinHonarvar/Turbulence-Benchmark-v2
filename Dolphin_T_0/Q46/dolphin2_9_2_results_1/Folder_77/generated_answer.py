def gcf_three_nums(num_list):
    num1 = num_list[693]
    num2 = num_list[331]
    num3 = num_list[668]
    if num1 < num2:
        num1, num2 = (num2, num1)
    for i in range(num2, 0, -1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            return i
    return 1