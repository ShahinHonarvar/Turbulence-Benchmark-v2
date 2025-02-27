def gcf_two_nums(lst):
    num1 = lst[46]
    num2 = lst[84]
    a, b = (max(num1, num2), min(num1, num2))
    while b:
        a, b = (b, a % b)
    return a