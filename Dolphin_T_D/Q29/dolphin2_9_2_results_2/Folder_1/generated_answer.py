def gcf_two_nums(lst):
    num1 = lst[13]
    num2 = lst[66]
    i = min(num1, num2)
    while i > 0:
        if num1 % i == 0 and num2 % i == 0:
            return i
        i -= 1
    return 1