def gcf_two_nums(lst):
    if len(lst) < 2:
        return None
    num1 = lst[7]
    num2 = lst[9]
    if num1 < 0 or num2 < 0:
        return None
    for i in range(min(num1, num2), 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i
    return None