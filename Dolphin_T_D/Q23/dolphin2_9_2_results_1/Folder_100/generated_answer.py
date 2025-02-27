def find_divisors_in_range(n):
    divisors = []
    i = 11
    while i <= 41:
        if n % i == 0:
            divisors.append(i)
        i += 1
    return divisors