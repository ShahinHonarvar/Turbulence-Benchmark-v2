def all_right_truncatable_prime(args):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        while len(str(n)) > 1:
            if not is_prime(n):
                return False
            n = int(str(n)[:-1])
        return is_prime(n)
    x = args[10]
    primes = [i for i in range(2, x) if is_prime(i) and is_right_truncatable_prime(i)]
    primes.sort(reverse=True)
    return primes