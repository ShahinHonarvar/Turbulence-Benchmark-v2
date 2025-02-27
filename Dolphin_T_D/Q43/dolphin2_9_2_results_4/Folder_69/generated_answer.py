def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    primes = [lst[i] for i in range(497, 931) if is_prime(lst[i])]
    return sorted(primes, reverse=True)