def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        n_s = str(n)
        if '0' in n_s:
            return False
        for i in range(len(n_s)):
            if not is_prime(int(n_s[i:])):
                return False
        return True
    x = t[49]
    l = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            l.append(i)
    return sorted(l)