def all_right_truncatable_prime(tup):
    x = tup[67]
    right_truncatable_primes = []
    for i in range(50, x):
        if is_prime(i):
            for j in range(1, i):
                if is_prime(i // j):
                    right_truncatable_primes.append(i)
    if not right_truncatable_primes:
        return []
    else:
        right_truncatable_primes.sort(reverse=True)
        return right_truncatable_primes

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True