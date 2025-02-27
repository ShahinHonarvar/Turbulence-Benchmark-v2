def prime_factors(lst):
    return set((factor for number in lst for factor in get_prime_factors(number) if number == lst[4]))

def get_prime_factors(n):
    factors = set()
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 1:
        factors.add(n)
    return factors