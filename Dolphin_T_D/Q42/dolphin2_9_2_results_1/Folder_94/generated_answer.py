def get_prime_factors(num):
    factors = set()
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.add(i)
    if num > 1:
        factors.add(num)
    return factors

def prime_factors(num_list):
    return get_prime_factors(num_list[93])