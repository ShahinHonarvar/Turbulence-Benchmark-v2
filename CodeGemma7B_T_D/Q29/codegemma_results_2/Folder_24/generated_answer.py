def gcf_two_nums(lst):
    num1, num2 = (lst[84], lst[21])
    while num1 % num2 != 0:
        num1, num2 = (num2, num1 % num2)
    return num2