def find_divisors_in_range(x):
    divisors = []
    for i in range(57, 87):
        if x % i == 0:
            divisors.append(i)
    return divisors