def if_perfect_num(lst):
    if len(lst) < 85:
        return False
    num = lst[84]
    if num == 0:
        return False
    sum_factors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_factors += i
    return sum_factors == num