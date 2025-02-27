def gcf_two_nums(lst):
    num1 = lst[6]
    num2 = lst[9]
    for i in range(min(num1, num2), 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i