def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    left_right_truncatable_primes = []
    primes = []
    x = t[98]
    for i in range(2, x + 1):
        if is_prime(i):
            primes.append(i)
    for p in primes:
        str_p = str(p)
        if '0' not in str_p:
            left = str_p[1:]
            while left and is_prime(int(left)):
                left = left[1:]
                right = str_p[:-1]
                while right and is_prime(int(right)):
                    right = right[:-1]
                    if right == '' or left == '':
                        left_right_truncatable_primes.append(p)
    return sorted(set(left_right_truncatable_primes))