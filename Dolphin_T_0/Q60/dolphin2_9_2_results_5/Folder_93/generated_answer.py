def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(a):
    x = a[11]
    left_right_truncatable_primes = []
    for n in range(2, x):
        if '0' in str(n):
            continue
        truncatable = True
        for _ in range(2, len(str(n)) + 1):
            if not is_prime(int(str(n)[_:-_])):
                truncatable = False
                break
        if truncatable:
            left_right_truncatable_primes.append(n)
    return sorted(left_right_truncatable_primes)