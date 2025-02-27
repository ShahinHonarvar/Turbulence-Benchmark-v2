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

    def truncate_left(n):
        return int(str(n)[1:])
    x = t[70]
    left_truncatable_primes = []
    for i in range(x - 1, 1, -1):
        if '0' not in str(i) and all((is_prime(int(str(i)[:j])) for j in range(len(str(i)), 0, -1))):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)