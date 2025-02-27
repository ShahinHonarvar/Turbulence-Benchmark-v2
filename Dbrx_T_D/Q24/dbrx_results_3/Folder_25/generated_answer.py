def sum_of_divisors_in_range(n):
    divisors = set()
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.add(i)
    divisors_in_range = divisors.intersection(set(range(84, 87)))
    return sum(divisors_in_range)