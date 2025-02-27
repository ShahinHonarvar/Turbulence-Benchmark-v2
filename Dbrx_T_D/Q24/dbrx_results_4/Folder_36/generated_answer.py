def sum_of_divisors_in_range(n):
    divisors_sum = 0
    for i in range(1, n + 1):
        if n % i == 0 and 113 <= i <= 991:
            divisors_sum += i
    if divisors_sum == 0:
        return 0
    else:
        return divisors_sum