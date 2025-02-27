def sum_of_divisors_in_range(n):
    div_sum = 0
    for i in range(1, n + 1):
        if n % i != 0:
            continue
        div_sum += i
    if 50 <= div_sum <= 81:
        return div_sum
    return 0