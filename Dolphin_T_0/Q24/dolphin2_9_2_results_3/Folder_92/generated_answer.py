def sum_of_divisors_in_range(x):
    divisors = []
    for i in range(1, x + 1):
        if x % i == 0 and 8 <= i <= 9:
            divisors.append(i)
    if len(divisors) == 0:
        return 0
    else:
        return sum(divisors)