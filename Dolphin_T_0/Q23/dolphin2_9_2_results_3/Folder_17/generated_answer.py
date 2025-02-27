def find_divisors_in_range(n):
    divisors = []
    i = 10
    while i <= 69 and i <= n:
        if n % i == 0:
            divisors.append(i)
        i += 1
    return divisors