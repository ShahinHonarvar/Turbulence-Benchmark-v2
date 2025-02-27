def if_perfect_num(lst):
    perfect_num = lst[51]
    sum_proper_divisors = 0
    for i in range(1, perfect_num):
        if perfect_num % i == 0:
            sum_proper_divisors += i
    return sum_proper_divisors == perfect_num