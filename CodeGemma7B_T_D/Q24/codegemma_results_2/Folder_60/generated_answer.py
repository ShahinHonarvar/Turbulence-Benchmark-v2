def sum_of_divisors_in_range(n):
    if n <= 0:
        return 0
    divisors = []
    for i in range(41, 56):
        if n % i == 0:
            divisors.append(i)
    if not divisors:
        return 0
    return sum(divisors)