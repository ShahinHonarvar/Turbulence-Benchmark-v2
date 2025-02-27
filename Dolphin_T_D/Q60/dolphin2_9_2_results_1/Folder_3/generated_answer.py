def all_left_right_truncatable_prime(n):

    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True
    x = n[100]
    left_right_truncatable_primes = []
    for i in range(1, x + 1):
        if is_prime(i):
            s = str(i)
            while len(s) > 1:
                if '0' in s or not is_prime(int(s[1:-1])) or (not is_prime(int(s[:-1]))):
                    break
                s = s[1:-1]
            if len(s) == 1 and is_prime(int(s)):
                left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes)