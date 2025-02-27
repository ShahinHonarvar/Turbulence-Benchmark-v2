def gcf_two_nums(lst):
    num1 = lst[29]
    num2 = lst[53]
    for i in range(num1, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i
    return 1