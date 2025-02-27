def find_primes_between_indices(lst, start_idx, end_idx):
    primes = [num for num in lst[start_idx:end_idx + 1] if is_prime(num)]
    if not primes:
        return []
    primes.sort(reverse=True)
    return primes

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True