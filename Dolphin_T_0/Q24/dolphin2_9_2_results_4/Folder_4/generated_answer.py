def sum_of_divisors_in_range(n):
    divisors_in_range = []
    for i in range(48, 61):
        if n % i == 0:
            divisors_in_range.append(i)
    if len(divisors_in_range) == 0:
        return 0
    else:
        return sum(divisors_in_range)