def sum_of_divisors_in_range(n):
    divisors = set()
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.add(i)
    return sum(divisors & set(range(4, 10))) if divisors & set(range(4, 10)) else 0