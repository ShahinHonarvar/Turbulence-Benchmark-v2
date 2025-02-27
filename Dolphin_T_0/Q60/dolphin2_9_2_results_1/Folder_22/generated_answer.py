def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        m = int(n ** 0.5) + 1
        for x in range(3, m, 2):
            if n % x == 0:
                return False
        return True

    def left_right_truncatable(s):
        while len(s) > 2:
            if s[:-1] == '0':
                return False
            if s[:1] + s[-1] not in primes:
                return False
            s = s[1:-1]
        if s != '2' and s != '3':
            return False
        return True
    global primes
    primes = [2, 3, 5, 7]
    x = x % 1000
    for p in range(11, x, 2):
        if is_prime(p):
            primes.append(p)
    lrt_primes = []
    for p in primes:
        if str(p)[::-1] == str(p).replace('0', '') and left_right_truncatable(str(p).replace('0', '')):
            lrt_primes.append(p)
    return sorted(lrt_primes)