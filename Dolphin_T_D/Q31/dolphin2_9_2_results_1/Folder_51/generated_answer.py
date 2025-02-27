def if_perfect_num(lst):
    if len(lst) < 65:
        return False
    num = lst[64]
    sum_of_factors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_factors += i
    if sum_of_factors == num:
        return True
    else:
        return False