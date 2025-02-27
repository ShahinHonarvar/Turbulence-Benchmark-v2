import itertools

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(x):
    primes = [i for i in range(2, int(x)) if is_prime(i)]
    left_truncatable = [i for i in primes if all(is_prime((int((''.join(j) for j in itertools.combinations(str(i), k))) for k in range(1, len(str(i))))))]
    return sorted(list(left_truncatable), reverse=True)

def all_left_truncatable_prime(t):
    return left_truncatable_prime(t[97])