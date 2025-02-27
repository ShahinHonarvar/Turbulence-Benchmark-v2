def all_left_truncatable_prime(t):
    x = t[84]
    left_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            trunc_num = i
            while trunc_num > 0:
                if not is_prime(trunc_num):
                    break
                left_truncatable_primes.append(trunc_num)
                trunc_num //= 10
    left_truncatable_primes.sort(reverse=True)
    return left_truncutable_primes

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True