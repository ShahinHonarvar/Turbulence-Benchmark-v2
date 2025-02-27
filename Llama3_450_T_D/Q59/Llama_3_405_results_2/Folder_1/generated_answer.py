def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[20]
    left_truncatable_primes = []
    for num in range(11, x):
        if '0' in str(num):
            continue
        is_truncatable = True
        for i in range(len(str(num))):
            if not is_prime(int(str(num)[i:])):
                is_truncatable = False
                break
        if is_truncatable:
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)