def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[86]
    left_truncatable_primes = []
    for i in range(10, x):
        s = str(i)
        if '0' not in s and is_prime(i):
            prime = True
            for j in range(1, len(s)):
                if not is_prime(int(s[j:])):
                    prime = False
                    break
            if prime:
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)