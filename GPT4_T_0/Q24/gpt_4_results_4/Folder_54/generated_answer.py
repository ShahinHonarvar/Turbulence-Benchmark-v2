def sum_of_divisors_in_range(n):
    sum_divisors = 0
    for i in range(36, 94):
        if n % i == 0:
            sum_divisors += i
    return sum_divisors