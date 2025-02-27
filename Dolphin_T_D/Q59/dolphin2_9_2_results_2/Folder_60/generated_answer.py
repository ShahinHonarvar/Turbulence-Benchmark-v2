def all_left_truncatable_prime(t):
    x = t[87]

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

    def is_left_truncatable_prime(n):
        n = str(n)
        if '0' in n:
            return False
        for i in range(1, len(n)):
            if not is_prime(int(n[i:] + n[:i])):
                return False
        return True
    all_left_truncatable_primes = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            all_left_truncatable_primes.append(i)
    return sorted(all_left_truncatable_primes)