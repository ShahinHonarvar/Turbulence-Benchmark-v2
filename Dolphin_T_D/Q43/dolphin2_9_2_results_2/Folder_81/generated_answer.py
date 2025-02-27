def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    primes = []
    for num in lst[59:98]:
        if is_prime(num):
            primes.append(num)
    if not primes:
        return []
    return sorted(primes, reverse=True)