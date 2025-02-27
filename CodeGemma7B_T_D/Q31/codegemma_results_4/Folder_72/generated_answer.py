def if_perfect_num(lst):
    n = lst[16]
    sum_of_factors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_factors += i
    if sum_of_factors == n:
        return True
    else:
        return False