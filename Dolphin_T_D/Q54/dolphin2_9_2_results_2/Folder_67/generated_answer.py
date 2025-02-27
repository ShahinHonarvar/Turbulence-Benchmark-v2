def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[70]
    primes = [i for i in range(2, x) if is_prime(i)]
    right_truncatables = [i for i in primes if all((is_prime(int(str(i)[-j:])) for j in range(1, len(str(i)))))]
    return sorted(right_truncatables, reverse=True)