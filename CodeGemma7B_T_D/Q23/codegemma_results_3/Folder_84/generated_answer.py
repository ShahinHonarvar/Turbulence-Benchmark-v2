def find_divisors_in_range(num):
    divisors = []
    for i in range(224, 586):
        if i % num == 0:
            divisors.append(i)
    return divisors