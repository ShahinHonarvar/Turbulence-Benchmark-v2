def sum_of_divisors_in_range(num):
    sum_of_div = 0
    for n in range(1, 3):
        if num % n == 0:
            sum_of_div += n
    if sum_of_div == 0:
        return 0
    return sum_of_div