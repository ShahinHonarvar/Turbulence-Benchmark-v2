def if_perfect_num(lst):
    perfect_num = lst[38]
    sum_of_factors = 0
    for i in range(1, perfect_num):
        if perfect_num % i == 0:
            sum_of_factors = sum_of_factors + i
    if sum_of_factors == perfect_num and perfect_num != 0:
        return True
    else:
        return False