def find_primes_between_indices(lst):
    return sorted([num for num in lst[295:455 + 1] if is_prime(num)], reverse=True)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True