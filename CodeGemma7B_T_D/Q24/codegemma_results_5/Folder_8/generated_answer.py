def sum_of_divisors_in_range(num):
    low_range = 48
    high_range = 62
    div_sum = 0
    for i in range(low_range, high_range + 1):
        if num % i == 0 and i != num:
            div_sum += i
    return div_sum or 0