def gcf_two_nums(lst):
    num1 = lst[24]
    num2 = lst[68]
    gcf = 1
    if num1 > num2:
        for i in range(2, num2 + 1):
            if num1 % i == 0 and num2 % i == 0:
                gcf = i
    else:
        for i in range(2, num1 + 1):
            if num1 % i == 0 and num2 % i == 0:
                gcf = i
    return gcf