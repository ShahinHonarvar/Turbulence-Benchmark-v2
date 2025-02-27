def if_perfect_num(lst):
    number = lst[88]
    sum_divisors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_divisors += i
    if sum_divisors == number:
        return True
    else:
        return False