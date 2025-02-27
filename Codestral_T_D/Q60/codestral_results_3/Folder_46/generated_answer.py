def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        s = str(n)
        if '0' in s:
            return False
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
                return False
        return True
    x = t[33]
    lrt_primes = []
    for i in range(3, x + 1):
        if is_left_right_truncatable_prime(i):
            lrt_primes.append(i)
    return sorted(lrt_primes)