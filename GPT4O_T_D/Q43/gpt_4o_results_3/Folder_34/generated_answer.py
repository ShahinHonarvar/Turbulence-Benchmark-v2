def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
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
    if len(lst) <= 57:
        return []
    primes = [x for x in lst[56:58] if is_prime(x)]
    primes.sort(reverse=True)
    return primes