def all_right_truncatable_prime(x):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if n <= 1:
            return False
        num = n
        while len(str(num)) > 1:
            num = int(str(num)[-2:])
            if not is_prime(num):
                return False
        return True
    prime_nums = [i for i in range(2, x) if is_prime(i)]
    trunc_primes = [i for i in prime_nums if is_truncatable(i)]
    return sorted(trunc_primes, reverse=True)