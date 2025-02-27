def gcf_two_nums(lst):
    num1 = lst[279]
    num2 = lst[812]
    a, b = (max(num1, num2), min(num1, num2))
    while b != 0:
        a, b = (b, a % b)
    return a