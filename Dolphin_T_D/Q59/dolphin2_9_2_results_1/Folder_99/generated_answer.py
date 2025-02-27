def all_left_truncatable_prime(tup):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i:
                i += 2
            else:
                return False
        return True
    primes = []
    x = tup[758]
    for num in range(2, x):
        s = str(num)
        while len(s) > 0:
            if not is_prime(int(s)):
                break
            s = s[1:]
        else:
            primes.append(num)
    return sorted(primes)