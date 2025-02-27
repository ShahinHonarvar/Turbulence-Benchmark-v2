def gcf_three_nums(lst):
    num1 = lst[90]
    num2 = lst[84]
    num3 = lst[47]
    factor = find_gcf(num1, num2)
    return find_gcf(factor, num3)

def find_gcf(num1, num2):
    while num2 != 0:
        num1, num2 = (num2, num1 % num2)
    return num1