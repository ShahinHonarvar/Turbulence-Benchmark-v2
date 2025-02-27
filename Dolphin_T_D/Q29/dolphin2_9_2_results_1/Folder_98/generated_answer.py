def gcf_two_nums(lst):
    num1 = lst[0]
    num2 = lst[9]
    if num1 == 0 or num2 == 0:
        return 0
    for i in range(min(num1, num2), 1, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i
    return 1