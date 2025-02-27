def all_right_truncatable_prime(args):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    limit = args[0]
    right_truncatable_primes = [i for i in range(2, limit) if right_truncatable_prime(i) and is_prime(i)]
    return sorted(right_truncatable_primes, reverse=True)