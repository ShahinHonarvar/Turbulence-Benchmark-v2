def all_right_truncatable_prime(t):

    def check_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def check_right_truncatable(n):
        n = str(n)
        while n:
            if not check_prime(int(n)):
                return False
            n = n[:-1]
        return True
    x = t[65]
    primes = [i for i in range(2, x) if check_prime(i)]
    right_truncatables = [i for i in primes if check_right_truncatable(i)]
    return sorted(right_truncatables, reverse=True)