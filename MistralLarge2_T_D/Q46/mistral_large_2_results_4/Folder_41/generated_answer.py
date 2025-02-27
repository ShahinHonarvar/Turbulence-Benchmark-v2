def gcf(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_three_nums(lst):
    num1 = lst[19]
    num2 = lst[94]
    num3 = lst[78]
    return gcf(gcf(num1, num2), num3)