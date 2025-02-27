def all_left_truncatable_prime(args):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        while n:
            if n < 10:
                n = n * 10
            n = n // 10
            if not is_prime(n):
                return False
        return True

    def get_truncatable_primes(n):

        def helper(n, left, primes):
            if is_truncatable_prime(n):
                primes.append(n)
            else:
                return
            for n in helper(n - 1, left - 1, primes) if left else []:
                if is_truncatable_prime(n):
                    primes.append(n)
            return primes
        return helper(n, len(str(n)), [])
    x = args[25]
    primes = get_truncatable_primes(x - 1)
    primes.reverse()
    return primes