def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(list_of_integers):
    primes = []
    for n in list_of_integers[157:736]:
        if is_prime(n):
            primes.append(n)
    if len(primes) > 0:
        return sorted(primes, reverse=True)
    else:
        return []