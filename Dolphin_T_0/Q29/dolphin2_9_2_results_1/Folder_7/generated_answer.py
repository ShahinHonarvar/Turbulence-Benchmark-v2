def gcf_two_nums(lst):
    num1 = lst[224]
    num2 = lst[663]
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1
    for i in range(1, smaller + 1):
        if smaller % i == 0 and num1 % i == 0 and (num2 % i == 0):
            gcf = i
    return gcf