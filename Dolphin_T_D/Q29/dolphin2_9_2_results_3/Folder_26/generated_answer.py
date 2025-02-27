def gcf_two_nums(lst):
    if len(lst) < 50 or len(lst) < 32:
        raise ValueError('Input list must contain at least 50 elements')
    num1 = lst[49]
    num2 = lst[31]
    gcf = 1
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
    return gcf