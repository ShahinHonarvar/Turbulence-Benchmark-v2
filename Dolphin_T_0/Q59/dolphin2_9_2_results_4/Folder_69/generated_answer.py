def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(p):
        p_str = str(p)
        for i in range(1, len(p_str)):
            if not is_prime(int(p_str[i:])):
                return False
        return True
    x = t[760]
    res = []
    for i in range(x):
        if is_truncatable(i) and is_prime(i):
            res.append(i)
    res.sort(reverse=True)
    return res