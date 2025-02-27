def gcf_two_nums(lst):
    num1 = lst[84]
    num2 = lst[21]
    if num1 < num2:
        num1, num2 = (num2, num1)
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1