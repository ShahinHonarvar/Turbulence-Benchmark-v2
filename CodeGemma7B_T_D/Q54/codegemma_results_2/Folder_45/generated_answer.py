def all_right_truncatable_prime(n):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_rt_prime(n):
        if not is_prime(n):
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    rt_primes = []
    for i in range(2, n):
        if is_rt_prime(i):
            rt_primes.append(i)
    rt_primes.sort()
    return rt_primes