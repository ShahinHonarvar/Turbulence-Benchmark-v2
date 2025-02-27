def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    if len(lst) < 449:
        return []
    sublist = lst[413:449]
    primes = [num for num in sublist if is_prime(num)]
    return sorted(primes)