def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(3, 7):
        if n % i == 0:
            divisors.append(i)
    if divisors:
        return sum(divisors)
    else:
        return 0