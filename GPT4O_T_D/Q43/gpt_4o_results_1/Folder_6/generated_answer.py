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
    if len(lst) < 94:
        return []
    primes_in_range = [num for num in lst[89:94] if is_prime(num)]
    return sorted(primes_in_range, reverse=True)