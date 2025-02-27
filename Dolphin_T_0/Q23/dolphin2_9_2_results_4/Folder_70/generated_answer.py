def find_divisors_in_range(n):
    divisors = []
    i = 586
    while i <= 840:
        if n % i == 0:
            divisors.append(i)
        i += 1
    return divisors