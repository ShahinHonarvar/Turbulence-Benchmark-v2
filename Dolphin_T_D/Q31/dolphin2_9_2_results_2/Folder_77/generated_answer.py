def if_perfect_num(lst):
    num = lst[985]
    sum_of_factors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_factors += i
    if sum_of_factors == num:
        return True
    else:
        return False