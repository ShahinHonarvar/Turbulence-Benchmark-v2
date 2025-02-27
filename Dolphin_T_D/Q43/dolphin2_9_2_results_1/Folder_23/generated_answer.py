def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    result = []
    for i in range(20, 49):
        if is_prime(lst[i]):
            result.append(lst[i])
    return sorted(result, reverse=True)