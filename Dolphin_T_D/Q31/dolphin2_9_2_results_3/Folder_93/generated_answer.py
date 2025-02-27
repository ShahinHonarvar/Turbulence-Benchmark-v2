def if_perfect_num(lst):
    if len(lst) < 46:
        return False
    number = lst[45]
    sum_proper_divisors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_proper_divisors += i
    return sum_proper_divisors == number