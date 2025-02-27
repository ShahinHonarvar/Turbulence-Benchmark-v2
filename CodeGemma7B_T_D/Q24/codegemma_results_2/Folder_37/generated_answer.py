def sum_of_divisors_in_range(n):
    div = 0
    for i in range(3, 8):
        if n % i == 0:
            div += i
    return div