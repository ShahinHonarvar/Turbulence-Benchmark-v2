def gcf_two_nums(lst):
    num1 = lst[8]
    num2 = lst[9]
    if num1 > num2:
        while num2 != 0:
            num1, num2 = (num2, num1 % num2)
        return num1
    else:
        while num1 != 0:
            num2, num1 = (num1, num2 % num1)
        return num2