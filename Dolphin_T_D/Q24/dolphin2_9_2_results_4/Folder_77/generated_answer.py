def sum_of_divisors_in_range(integer):
    integer_range = range(111, 509)
    div_sum = 0
    for i in integer_range:
        if integer % i == 0:
            div_sum += i
    if div_sum == 0:
        return 0
    return div_sum