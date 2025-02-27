def all_left_truncatable_prime(t):

    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def is_truncatable_prime(n):
        if n == 2:
            return True
        str_n = str(n)
        for i in range(len(str_n) - 1, 0, -1):
            if str_n[:i] == '' or not is_prime(int(str_n[:i])):
                return False
        return True
    x = t[30]
    primes = []
    for i in range(2, x):
        if is_truncatable_prime(i):
            primes.append(i)
    primes.sort()
    return primes