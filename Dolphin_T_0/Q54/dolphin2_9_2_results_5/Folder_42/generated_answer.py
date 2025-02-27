def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(num_tuple):
    x = num_tuple[64]
    right_truncatable_primes = []
    for i in range(x):
        if is_prime(i):
            j = i
            while j > 0 and is_prime(j):
                j //= 10
            if j == 0:
                right_truncatable_primes.append(i)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes