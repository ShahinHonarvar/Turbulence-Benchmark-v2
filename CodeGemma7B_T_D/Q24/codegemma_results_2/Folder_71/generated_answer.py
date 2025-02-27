def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(45, 73):
        if n % i == 0:
            divisors.append(i)
    if not divisors:
        return 0
    return sum(divisors)