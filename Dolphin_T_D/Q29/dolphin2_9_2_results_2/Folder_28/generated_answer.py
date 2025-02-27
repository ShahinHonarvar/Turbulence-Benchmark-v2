def gcf_two_nums(lst):
    num1 = lst[48]
    num2 = lst[76]
    if num1 == 0 and num2 == 0:
        return 0
    else:
        a = min(num1, num2)
        b = max(num1, num2)
        while b % a != 0:
            c = b % a
            a = c
            b = b - c
        return a