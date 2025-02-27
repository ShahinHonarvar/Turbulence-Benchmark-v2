def sum_of_divisors_in_range(num):
    """This function finds the sum of all positive divisors between 46 and 89 in num."""
    total_sum = 0
    for i in range(46, 90):
        if i == 0:
            continue
        if num % i == 0:
            total_sum += i
    if total_sum > 0:
        return total_sum
    else:
        return 0