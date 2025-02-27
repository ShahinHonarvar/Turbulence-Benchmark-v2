def if_perfect_num(lst):
    if len(lst) > 57:
        num = lst[57]
        sum_div = 0
        for i in range(1, num):
            if num % i == 0:
                sum_div += i
        return sum_div == num
    else:
        return False