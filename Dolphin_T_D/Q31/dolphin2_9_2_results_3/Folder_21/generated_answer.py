def if_perfect_num(lst):
    index = lst[410]
    sum_divisors = 0
    for i in range(1, index):
        if index % i == 0:
            sum_divisors += i
    if sum_divisors == index:
        return True
    return False