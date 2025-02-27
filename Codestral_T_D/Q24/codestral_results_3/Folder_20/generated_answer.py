def sum_of_divisors_in_range(n):
    div_sum = 0
    for i in range(28, 82):
        if n % i == 0:
            div_sum += i
    return div_sum