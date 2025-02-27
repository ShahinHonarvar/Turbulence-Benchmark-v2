def if_perfect_num(lst):
    if len(lst) < 75:
        return False
    number = lst[74]
    sum_factors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_factors += i
    return sum_factors == number