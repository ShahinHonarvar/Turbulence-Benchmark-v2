def all_right_truncatable_prime(t):
    x = t[73]

    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i:
                i += 2
            else:
                return False
        return True

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n > 1:
            if not is_prime(n):
                return False
            n //= 10
        return True
    l = []
    if x < 2:
        return l
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            l.append(i)
    l.sort(reverse=True)
    return l