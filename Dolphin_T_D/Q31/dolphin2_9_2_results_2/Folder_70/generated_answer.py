def if_perfect_num(lst):
    if len(lst) > 845:
        num = lst[845]
        sum_div = sum((i for i in range(1, num) if num % i == 0))
        if sum_div == num:
            return True
    return False