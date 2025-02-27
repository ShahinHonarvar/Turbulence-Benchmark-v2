def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        s = str(n)
        while len(s) > 1:
            if not is_prime(int(s)):
                return False
            s = s[:-1]
        return True
    x = t[78]
    l = []
    for i in range(2, x):
        if is_prime(i) and is_right_truncatable(i):
            l.append(i)
    l.sort(reverse=True)
    return l