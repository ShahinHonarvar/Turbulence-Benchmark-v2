def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n == 1:
            return False
        p = 3
        while p * p <= n and n % p != 0:
            p += 2
        return p * p > n
    truncatable_primes = []
    for i in range(2, x + 1):
        if '0' in str(i):
            continue
        while i > 0:
            if not is_prime(i):
                break
            truncatable_primes.append(i)
            i = int(str(i)[1:-1])
    return list(set(truncatable_primes))[::-1]