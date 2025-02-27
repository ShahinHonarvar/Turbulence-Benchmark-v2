def if_perfect_num(lst):
    perfect_number = 6
    sum_of_divisors = 1
    for i in range(2, perfect_number):
        if perfect_number % i == 0:
            sum_of_divisors += i
    return lst[72] == perfect_number