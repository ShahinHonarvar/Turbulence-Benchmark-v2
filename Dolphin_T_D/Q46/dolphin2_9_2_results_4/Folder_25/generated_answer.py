def gcf_three_nums(lst):
    num1 = lst[32]
    num2 = lst[54]
    num3 = lst[13]
    i = min(num1, num2, num3)
    while i > 1:
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            return i
        i -= 1
    return 1