def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    start = 187
    end = 271
    primes = []
    for i in lst[start:end + 1]:
        if is_prime(i):
            primes.append(i)
    return sorted(primes)