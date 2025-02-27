def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    result = []
    for i in range(46, min(86, len(lst))):
        if is_prime(lst[i]):
            result.append(lst[i])
    return sorted(result)