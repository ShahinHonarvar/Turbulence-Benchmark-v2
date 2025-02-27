def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    primes = []
    for num in lst[13:69]:
        if is_prime(num):
            primes.append(num)
    primes.sort()
    return primes