def gcf_two_nums(lst):
    num1 = lst[224]
    num2 = lst[663]
    if num1 == 0 and num2 == 0:
        return 0
    num1, num2 = (min(num1, num2), max(num1, num2))
    while num2 % num1 != 0:
        num1, num2 = (num2 % num1, num1)
    return num1