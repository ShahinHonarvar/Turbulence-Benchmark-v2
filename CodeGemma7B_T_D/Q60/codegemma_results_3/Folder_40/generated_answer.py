def all_left_right_truncatable_prime(a):
    a = a[10]
    left_truncatable_primes = []
    right_truncatable_primes = []
    for i in range(2, a + 1):
        if is_prime(i):
            if is_left_truncatable_prime(i) and is_right_truncatable_prime(i):
                left_truncatable_primes.append(i)
                right_truncatable_primes.append(i)
    left_truncatable_primes.sort(reverse=True)
    right_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes + right_truncatable_primes

def is_left_truncatable_prime(i):
    if '0' in str(i):
        return False
    while i > 1:
        if not is_prime(i):
            return False
        i = int(str(i)[:-1])
    return True

def is_right_truncatable_prime(i):
    if '0' in str(i):
        return False
    while i > 1:
        if not is_prime(i):
            return False
        i = int(str(i)[1:])
    return True

def is_prime(i):
    if i <= 1:
        return False
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            return False
    return True