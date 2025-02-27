def if_perfect_num(lst):
    if len(lst) < 35:
        return False
    perfect_num = lst[34]
    sum_divisors = 0
    for i in range(1, perfect_num):
        if perfect_num % i == 0:
            sum_divisors += i
    if sum_divisors == perfect_num:
        return True
    else:
        return False