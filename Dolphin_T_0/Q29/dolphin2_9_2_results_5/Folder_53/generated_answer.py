def gcf_two_nums(lst):
    num1 = lst[28]
    num2 = lst[67]
    gcf = min(num1, num2)
    if gcf == 0:
        return None
    for i in range(1, gcf + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
    return gcf