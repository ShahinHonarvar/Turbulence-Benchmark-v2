def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        f = 3
        while f * f <= n:
            if n % f == 0:
                return False
            f += 2
        return True

    def truncate(s):
        if s[0] == '0':
            return ''
        else:
            return s
    x = t[50]
    primes = [i for i in range(x + 1) if is_prime(i)]
    left_right_truncatable = []
    for prime in primes:
        left_trunc = truncate(str(prime))
        while left_trunc != '':
            if not is_prime(int(left_trunc)):
                break
            left_trunc = truncate(left_trunc[1:])
        right_trunc = truncate(str(prime))
        while right_trunc != '':
            if not is_prime(int(right_trunc)):
                break
            right_trunc = truncate(right_trunc[:-1])
        if left_trunc == '' and right_trunc == '':
            left_right_truncatable.append(prime)
    return sorted(left_right_truncatable, reverse=True)