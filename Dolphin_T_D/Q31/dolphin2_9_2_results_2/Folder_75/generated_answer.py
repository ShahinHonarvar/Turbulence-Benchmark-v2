def if_perfect_num(lst):
    perfect_num = lst[80]
    sum_divisors = 0
    for i in range(1, perfect_num):
        if perfect_num % i == 0:
            sum_divisors += i
    if sum_divisors == perfect_num:
        return True
    else:
        return False