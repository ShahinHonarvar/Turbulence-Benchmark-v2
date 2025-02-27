def gcf_two_nums(lst):
    if len(lst) < 10:
        return None
    num1 = lst[8]
    num2 = lst[9]
    i = 1
    gcf = None
    while i <= num1 and i <= num2:
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
        i += 1
    return gcf