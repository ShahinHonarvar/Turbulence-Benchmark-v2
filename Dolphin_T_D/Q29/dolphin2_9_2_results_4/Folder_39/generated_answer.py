def gcf_two_nums(lst):
    num1 = lst[46]
    num2 = lst[13]
    a, b = (max(num1, num2), min(num1, num2))
    while b != 0:
        a, b = (b, a % b)
    return a