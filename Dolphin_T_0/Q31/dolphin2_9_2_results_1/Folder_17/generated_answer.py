def if_perfect_num(lst):
    if len(lst) >= 632:
        num = lst[631]
        sum_div = 1
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                sum_div += i
        return num == sum_div
    else:
        return False