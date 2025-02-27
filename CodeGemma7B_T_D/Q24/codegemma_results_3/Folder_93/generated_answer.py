def sum_of_divisors_in_range(N):
    div_sum = 0
    for num in range(48, 93):
        if N % num == 0:
            div_sum += num
    if div_sum == 0:
        return 0
    else:
        return div_sum