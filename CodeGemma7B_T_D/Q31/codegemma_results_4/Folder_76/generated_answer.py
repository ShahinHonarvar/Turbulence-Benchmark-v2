def if_perfect_num(lst):
    num = lst[537]
    sum_of_factors = 0
    for factor in range(1, num):
        if num % factor == 0:
            sum_of_factors += factor
    return sum_of_factors == num