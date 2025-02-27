def if_perfect_num(lst):
    if len(lst) < 49:
        return False
    num = lst[48]
    sum_of_factors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_factors += i
    return sum_of_factors == num