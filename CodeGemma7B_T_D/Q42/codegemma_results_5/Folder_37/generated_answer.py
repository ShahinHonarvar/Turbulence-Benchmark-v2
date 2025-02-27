def prime_factors(lst):
    prime_factors = set()
    integer = lst[28]
    for i in range(2, int(integer ** 0.5) + 1):
        if integer % i == 0:
            prime_factors.add(i)
            integer //= i
    if integer > 1:
        prime_factors.add(integer)
    return prime_factors