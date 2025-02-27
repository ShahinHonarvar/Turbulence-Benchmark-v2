def gcf_two_nums(lst):
    num1 = lst[47]
    num2 = lst[97]
    for i in range(min(num1, num2), 1, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i