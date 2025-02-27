def sum_of_divisors_in_range(n):
    divisors = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i:
            continue
        divisors.add(i)
        divisors.add(n // i)
    divisors = sorted(divisors)
    divisors_in_range = [d for d in divisors if 35 <= d <= 98]
    return sum(divisors_in_range) if divisors_in_range else 0