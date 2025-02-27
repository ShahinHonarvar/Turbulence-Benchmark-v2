def if_perfect_num(lst):
    perfect_num = lst[15]
    sum_of_factors = 0
    for i in range(1, perfect_num):
        if perfect_num % i == 0:
            sum_of_factors += i
    if sum_of_factors == perfect_num:
        return True
    else:
        return False