def sum_of_divisors_in_range(n):
    divisors, start, end = ([], 60, 86)
    for i in range(start, end + 1):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors) if len(divisors) > 0 else 0