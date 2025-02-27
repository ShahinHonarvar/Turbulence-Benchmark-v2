def gcf(a, b):
    while b > 0:
        a, b = (b, a % b)
    return a

def gcf_three_nums(lst):
    num1 = lst[99]
    num2 = lst[28]
    num3 = lst[53]
    gcf_num1_num2 = gcf(num1, num2)
    gcf_all = gcf(gcf_num1_num2, num3)
    return gcf_all