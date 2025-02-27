def if_perfect_num(lst):
    if len(lst) > 59:
        num = lst[59]
        sum_factors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_factors += i
        if num == sum_factors:
            return True
    return False