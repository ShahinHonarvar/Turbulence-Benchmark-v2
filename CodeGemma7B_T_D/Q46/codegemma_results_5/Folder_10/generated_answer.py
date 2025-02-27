def gcf_three_nums(lst):
    num1 = lst[86]
    num2 = lst[89]
    num3 = lst[49]
    result = find_gcf(num1, find_gcf(num2, num3))
    return result

def find_gcf(a, b):
    if b == 0:
        return a
    return find_gcf(b, a % b)