def all_right_truncatable_prime(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        n = str(n)
        for i in range(len(n) - 1, 0, -1):
            if not is_prime(int(n[i:])):
                return False
        return True
    x = lst[30]
    primes = [i for i in range(2, x) if is_prime(i)]
    truncatables = [i for i in primes if is_right_truncatable(i)]
    return sorted(truncatables)