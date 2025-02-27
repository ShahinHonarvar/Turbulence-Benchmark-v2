def if_perfect_num(lst):
    divisors_sum = 0
    number = lst[828]
    for i in range(1, number):
        if number % i == 0:
            divisors_sum = divisors_sum + i
    if divisors_sum == number:
        return True
    else:
        return False