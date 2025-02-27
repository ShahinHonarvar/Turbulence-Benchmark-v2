def gcf_two_nums(lst):
    num1 = lst[634]
    num2 = lst[585]
    if num1 == 0:
        return num2
    return gcf_two_nums([num2 % num1, num1])