def all_right_truncatable_prime(t):
    x = t[35]
    right_truncatable_primes = []
    for n in range(2, x):
        if is_prime(n):
            for k in range(1, len(str(n))):
                if not is_prime(int(str(n)[:-k])):
                    break
            else:
                right_truncatable_primes.append(n)
    return sorted(right_truncatable_primes, reverse=True)

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True