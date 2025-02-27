def all_left_truncatable_prime(Z):
    x = Z[64]
    left_truncatable_primes = []
    for i in range(2, x):
        n = i
        while True:
            if is_prime(n):
                left_truncatable = True
                for j in range(1, len(str(n))):
                    if not is_prime(int(str(n)[j:])):
                        left_truncatable = False
                        break
                if left_truncatable:
                    left_truncatable_primes.append(i)
            if n >= x:
                break
            n = n + 1
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True