def find_divisors_in_range(positive_integer):
    divisors = []
    for i in range(157, 903):
        if positive_integer % i == 0:
            divisors.append(i)
    return divisors