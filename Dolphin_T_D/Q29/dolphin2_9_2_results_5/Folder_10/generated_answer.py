def gcf_two_nums(lst):
    num1 = lst[15]
    num2 = lst[99]
    gcd = 1
    for i in range(1, min(num1, num2)):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
    return gcd