def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if n // i != i:
                divisors.append(n // i)
    filtered_divisors = [d for d in divisors if 59 <= d <= 88]
    if not filtered_divisors:
        return 0
    return sum(filtered_divisors)