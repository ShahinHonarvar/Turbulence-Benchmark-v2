def if_perfect_num(lst):
    perfect_number = lst[49]
    sum_divisors = 0
    for i in range(1, perfect_number):
        if perfect_number % i == 0:
            sum_divisors += i
    return sum_divisors == perfect_number