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

    def is_left_truncatable_prime(n):
        if n <= 1:
            return False
        m = n
        while m > 0:
            if m % 10 == 0:
                return False
            m //= 10
        strn = str(n)
        for i in range(len(strn)):
            if not is_prime(int(strn[:i + 1])):
                return False
        return True
    x = t[7]
    left_truncatable_primes = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)