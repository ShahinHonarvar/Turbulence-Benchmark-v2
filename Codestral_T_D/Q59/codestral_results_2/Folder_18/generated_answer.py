def all_left_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def truncate(n):
        return int(str(n)[1:])
    x = t[429]
    primes = [i for i in range(2, x) if is_prime(i)]
    left_truncatable_primes = []
    for p in primes:
        num = p
        while num > 0:
            if not is_prime(num):
                break
            num = truncate(num)
        if num == 0:
            left_truncatable_primes.append(p)
    return sorted(left_truncatable_primes, reverse=True)