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
    if not lst or len(lst) < 553:
        return []
    primes = []
    for index in range(424, 553):
        if is_prime(lst[index]):
            primes.append(lst[index])
    return sorted(primes, reverse=True)