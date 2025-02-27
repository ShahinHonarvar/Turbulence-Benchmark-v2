def find_divisors_in_range(integer):
    divisors = []
    for x in range(83, 96):
        if integer % x == 0:
            divisors.append(x)
    return divisors