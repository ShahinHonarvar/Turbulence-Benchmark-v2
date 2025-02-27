def find_divisors_in_range(integer):
    divisors = []
    for x in range(95, 83, -1):
        if integer % x == 0:
            divisors.append(x)
    return divisors