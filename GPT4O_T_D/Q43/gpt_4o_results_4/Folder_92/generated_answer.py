def is_prime(num):
    if num <= 1:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes_between_indices(lst):
    primes = []
    for i in range(7, min(9, len(lst))):
        if is_prime(lst[i]):
            primes.append(lst[i])
    return sorted(primes)