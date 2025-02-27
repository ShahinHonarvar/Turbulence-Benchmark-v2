def find_divisors_in_range(n):
    divisors = []
    i = 14
    while i <= 48:
        if n % i == 0:
            divisors.append(i)
        i += 1
    return divisors