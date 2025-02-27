def all_right_truncatable_prime(parameters):

    def is_prime(n):
        if n == 1:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True

    def trunc(n):
        if n < 10:
            return n == n
        t = n
        while t:
            t = int(t / 10)
            if not is_prime(t):
                return False
        return True
    x = parameters[38]
    right_truncatable_primes = [i for i in range(2, x) if is_prime(i) and trunc(i)]
    return right_truncatable_primes