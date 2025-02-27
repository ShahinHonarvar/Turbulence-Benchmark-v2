def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[89]
    l = []
    for i in range(x - 1, 1, -1):
        n = i
        while n:
            if n == 0 or not is_prime(n):
                break
            l.append(n)
            n *= 10
        if l:
            if len(set(l)) == len(l):
                return sorted(l, reverse=True)
    return l