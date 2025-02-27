def find_divisors_in_range(n):
    divisors = []
    i = 11
    while i <= 56:
        if n % i == 0:
            divisors.append(i)
        i += 1
    return divisors