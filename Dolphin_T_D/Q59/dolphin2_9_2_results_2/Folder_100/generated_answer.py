def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2 or n % 2 == 0:
            return n == 2
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    x = t[26]
    truncable_primes = [2]
    for n in range(3, x):
        if is_prime(n):
            s = str(n)
            if all((is_prime(int(s[i:])) and is_prime(int(s[i:][::-1])) for i in range(len(s)))):
                truncable_primes.append(n)
    return sorted(truncable_primes)