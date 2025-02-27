def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    primes = [lst[i] for i in range(len(lst)) if is_prime(lst[i]) and 7 <= i <= 8]
    return sorted(primes)