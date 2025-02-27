def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True

def find_primes_between_indices(lst):
    primes = [lst[i] for i in range(len(lst)) if is_prime(lst[i])]
    return sorted([i for i in primes if 131 <= lst.index(i) <= 815], reverse=True)