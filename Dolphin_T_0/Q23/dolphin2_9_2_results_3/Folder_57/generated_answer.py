def find_divisors_in_range(n):
    divisors = []
    i = 15
    while i <= 92:
        if n % i == 0:
            divisors.append(i)
        i += 1
    return divisors