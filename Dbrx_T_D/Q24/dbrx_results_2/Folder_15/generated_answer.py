def sum_of_divisors_in_range(n):
    divisors_sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            if 7 <= i <= 9:
                divisors_sum += i
    return divisors_sum