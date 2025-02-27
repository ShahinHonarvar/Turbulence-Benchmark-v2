def gcf_three_nums(lst):
    num1 = lst[21]
    num2 = lst[51]
    num3 = lst[33]
    i = 1
    while i <= 1:
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            result = i
        i += 1
    return result