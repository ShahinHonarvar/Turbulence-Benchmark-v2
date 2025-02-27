def find_divisors_in_range(integer):
    divisors = []
    for i in range(387, 517):
        if integer % i == 0:
            divisors.append(i)
    if len(divisors) == 0:
        return []
    return divisors