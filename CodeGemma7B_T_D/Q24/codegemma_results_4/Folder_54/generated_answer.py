def sum_of_divisors_in_range(n):
    if n <= 1:
        return 0
    sum_divisors = 0
    for i in range(36, 94):
        if n % i == 0:
            sum_divisors += i
    if sum_divisors == 0:
        return sum_divisors
    else:
        return sum_divisors