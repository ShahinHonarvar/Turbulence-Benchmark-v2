def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    divisors_in_range = [div for div in divisors if 18 <= div <= 52]
    if divisors_in_range:
        return sum(divisors_in_range)
    else:
        return 0