def gcf_two_nums(lst):
    if len(lst) < 70:
        return None
    num1 = lst[69]
    num2 = lst[40]
    i = min(num1, num2)
    while True:
        if num1 % i == 0 and num2 % i == 0:
            return i
        i -= 1