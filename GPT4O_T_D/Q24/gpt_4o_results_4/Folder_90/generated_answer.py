def sum_of_divisors_in_range(n):
    if n <= 0:
        return 0
    divisor_sum = 0
    start = max(451, 1)
    end = min(973, n)
    for i in range(start, end + 1):
        if n % i == 0:
            divisor_sum += i
    return divisor_sum