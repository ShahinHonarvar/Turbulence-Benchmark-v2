from sympy import isprime

def find_primes_between_indices(lst):
    primes = []
    for i in range(830, 850):
        if len(lst) > i:
            if isprime(lst[i]):
                primes.append(lst[i])
    return sorted(primes)