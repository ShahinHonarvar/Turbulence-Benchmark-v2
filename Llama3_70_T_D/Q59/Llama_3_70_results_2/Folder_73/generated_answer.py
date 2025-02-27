def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[97]
    left_truncatable_primes = []
    for i in range(2, x):
        if '0' not in str(i) and is_prime(i):
            num = str(i)
            is_left_truncatable = True
            for j in range(1, len(num)):
                if not is_prime(int(num[j:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)