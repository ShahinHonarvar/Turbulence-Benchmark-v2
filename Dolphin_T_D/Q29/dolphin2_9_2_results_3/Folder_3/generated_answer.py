def gcf_two_nums(lst):
    num1 = lst[47]
    num2 = lst[10]
    gcf = 1
    while num1:
        if num1 % num2 == 0:
            gcf = num2
            break
        num1, num2 = (num2, num1 % num2)
    return gcf