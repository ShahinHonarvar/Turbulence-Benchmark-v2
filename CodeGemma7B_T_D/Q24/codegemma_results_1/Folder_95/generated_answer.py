def sum_of_divisors_in_range(num):
    sum_div = 0
    for i in range(35, 99):
        if num % i == 0:
            sum_div += i
    if sum_div == 0:
        return 0
    else:
        return sum_div