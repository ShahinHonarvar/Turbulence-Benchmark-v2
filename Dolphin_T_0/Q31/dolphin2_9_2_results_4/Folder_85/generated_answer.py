def if_perfect_num(lst):
    num23 = lst[23]
    sum_factors = 0
    for i in range(1, num23):
        if num23 % i == 0:
            sum_factors += i
    return num23 == sum_factors