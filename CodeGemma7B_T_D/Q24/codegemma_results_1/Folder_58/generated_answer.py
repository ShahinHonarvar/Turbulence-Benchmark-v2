def sum_of_divisors_in_range(num):
    divisors = []
    for i in range(403, 515):
        if num % i == 0:
            divisors.append(i)
    if len(divisors) == 0:
        return 0
    else:
        return sum(divisors)