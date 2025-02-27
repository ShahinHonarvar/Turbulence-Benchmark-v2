def find_divisors_in_range(num):
    divisors = []
    for x in range(378, 783):
        if num % x == 0:
            divisors.append(x)
    return divisors