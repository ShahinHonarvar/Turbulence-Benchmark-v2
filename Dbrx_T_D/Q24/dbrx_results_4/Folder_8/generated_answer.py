def sum_of_divisors_in_range(n):
    divisors_sum = 0
    for i in range(1, int(n) + 1):
        if n % i == 0 and 48 <= i <= 62:
            divisors_sum += i
    return divisors_sum