def find_primes_between_indices(lst):
    primes = [num for num in lst[40:69] if isprime(num)]
    if not primes:
        return []
    return sorted(primes, reverse=True)

def isprime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True