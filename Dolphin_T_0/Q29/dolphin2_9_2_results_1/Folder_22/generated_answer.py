def gcf_two_nums(lst):
    if len(lst) < 69:
        return None
    num1 = lst[24]
    num2 = lst[68]
    for i in range(min(num1, num2), 1, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i
    return None