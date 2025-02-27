def find_divisors_in_range(positive_integer):
    divisors = []
    for i in range(60, 87):
        if positive_integer % i == 0:
            divisors.append(i)
    return divisors