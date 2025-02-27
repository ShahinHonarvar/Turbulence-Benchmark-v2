def all_right_truncatable_prime(a):
    x = a[835]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            for j in range(1, len(str(i))):
                if not is_prime(int(str(i)[:-j])):
                    break
            else:
                right_truncatable_primes.append(i)
    right_truncatable_primes.sort()
    return right_truncatable_primes

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True