def all_right_truncatable_prime(x):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n == 1:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def is_right_truncatable_prime(n):
        rev = str(n)[::-1]
        for i in range(len(rev) - 1):
            if not is_prime(int(rev[i:])):
                return False
        return True
    primes = []
    for n in range(2, x):
        if is_right_truncatable_prime(n):
            primes.append(n)
    return sorted(primes)