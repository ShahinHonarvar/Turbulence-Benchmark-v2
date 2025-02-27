def gcf_two_nums(lst):
    num1 = lst[872]
    num2 = lst[219]
    i = 2
    while i <= num1 and i <= num2:
        if num1 % i == 0 and num2 % i == 0:
            i += 1
        else:
            return i - 1
    return i - 1