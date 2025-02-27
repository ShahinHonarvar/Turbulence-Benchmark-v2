def if_perfect_num(lst):
    sum_of_proper_divisors = 0
    for i in range(1, lst[990]):
        if lst[990] % i == 0:
            sum_of_proper_divisors += i
    return sum_of_proper_divisors == lst[990]