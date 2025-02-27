def sum_of_divisors_in_range(n):
    div_sum = 0
    for i in range(3, 5):
        if n % i == 0:
            div_sum += i
    return div_sum