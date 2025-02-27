def gcf_two_nums(lst):
    num1 = lst[184]
    num2 = lst[307]
    a = max(num1, num2)
    b = min(num1, num2)
    while b:
        a, b = (b, a % b)
    return a