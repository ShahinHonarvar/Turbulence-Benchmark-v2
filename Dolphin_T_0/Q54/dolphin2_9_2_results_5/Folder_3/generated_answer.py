def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[100]
    primes = [2, 3, 5, 7]
    for i in range(11, x + 1):
        if is_prime(i):
            trunc = str(i)
            for j in range(1, len(trunc)):
                if is_prime(int(trunc[j:])):
                    primes.append(i)
    return sorted(list(set(primes)))