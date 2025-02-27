def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(42, 78):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors) if len(divisors) >= 1 else 0