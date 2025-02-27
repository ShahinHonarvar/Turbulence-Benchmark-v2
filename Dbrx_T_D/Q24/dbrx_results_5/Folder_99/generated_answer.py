def sum_of_divisors_in_range(n):
    divisors_sum = 0
    for i in range(1, n + 1):
        if n % i != 0:
            continue
        divisors_sum += i if 378 <= i <= 782 else 0
    return divisors_sum