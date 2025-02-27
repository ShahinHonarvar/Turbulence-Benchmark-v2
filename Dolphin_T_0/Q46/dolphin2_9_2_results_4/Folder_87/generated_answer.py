def gcf_three_nums(int_list):
    num1 = int_list[74]
    num2 = int_list[60]
    num3 = int_list[28]
    gcf = 1
    for i in range(1, min(num1, num2, num3) + 1):
        if num1 % i == num2 % i == num3 % i == 0:
            gcf = i
    return gcf