from math import sqrt

def prime_factors(lst):
    prime_facs = set()
    target_int = lst[263]
    for divisor in range(2, int(sqrt(target_int)) + 1):
        while target_int % divisor == 0:
            prime_facs.add(divisor)
            target_int //= divisor
    if target_int != 1:
        prime_facs.add(target_int)
    return prime_facs