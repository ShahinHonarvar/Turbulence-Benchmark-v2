def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    start, end = (lst[1], lst[3])
    primes = [num for num in lst[2:end + 1] if is_prime(num)]
    return sorted(primes)