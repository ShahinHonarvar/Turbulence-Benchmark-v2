def find_divisors_in_range(integer):
    divisors = []
    for i in range(43, 78):
        if i % integer == 0:
            divisors.append(i)
    return divisors