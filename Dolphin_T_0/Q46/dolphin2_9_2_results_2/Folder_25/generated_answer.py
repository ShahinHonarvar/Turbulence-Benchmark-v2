def gcf(a, b):
    if b == 0:
        return a
    else:
        return gcf(b, a % b)

def gcf_three_nums(lst):
    num1 = lst[32]
    num2 = lst[54]
    num3 = lst[13]
    gcf1n2 = gcf(num1, num2)
    return gcf(gcf1n2, num3)