from sympy import isprime

def find_primes_between_indices(lst):
    prime_numbers = []
    for i in range(60, 96):
        if i < len(lst) and isprime(lst[i]):
            prime_numbers.append(lst[i])
    return sorted(prime_numbers)