def sum_of_divisors_in_range(num):
    divisors = []
    for i in range(387, 517):
        if num % i == 0:
            divisors.append(i)
    if not divisors:
        return 0
    return sum(divisors)