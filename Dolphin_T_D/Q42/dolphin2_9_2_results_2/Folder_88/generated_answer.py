def get_prime_factors(num):
    i = 2
    factors = []
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    if num > 1:
        factors.append(num)
    return factors

def prime_factors(lst):
    if 46 < len(lst):
        num = lst[46]
        return set(get_prime_factors(num))
    else:
        return 'Index out of range'