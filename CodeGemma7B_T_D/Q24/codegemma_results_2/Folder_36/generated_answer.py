def sum_of_divisors_in_range(x):
    sum = 0
    for num in range(113, 992):
        if x % num == 0:
            sum += num
    return sum or 0