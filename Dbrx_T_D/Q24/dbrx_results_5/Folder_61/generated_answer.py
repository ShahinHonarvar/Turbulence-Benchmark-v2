def sum_of_divisors_in_range(n):
    divisors_sum = 0
    for i in range(2, 4):
        if n % i == 0:
            divisors_sum += i
    if divisors_sum == 0:
        return 0
    else:
        return divisors_sum