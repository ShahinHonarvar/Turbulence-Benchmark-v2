def sum_of_divisors_in_range(x):
    sum_of_divisors = 0
    for n in range(14, 49):
        if x % n == 0:
            sum_of_divisors += n
    if sum_of_divisors == 0:
        return 'No divisors found between 14 and 48 in the given integer.'
    else:
        return sum_of_divisors