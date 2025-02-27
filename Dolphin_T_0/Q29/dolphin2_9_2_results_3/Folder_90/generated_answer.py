def gcf_two_nums(lst):
    num1 = lst[634]
    num2 = lst[585]
    gcf = 1
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
    return gcf