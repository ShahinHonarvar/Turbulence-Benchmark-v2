def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n == 1:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if n < 10:
            return False
        if n < 100 and n % 10 == 0 and (n // 10 % 2 == 0):
            return True
        if n < 1000 and n % 10 == 0 and (n // 100 % 10 % 2 == 0):
            return True
        if n % 10 == 0:
            return False
        r = []
        while n > 0:
            r.append(n % 10)
            n //= 10
        if r[-1] % 2 == 0 or r[0] % 2 == 0:
            return False
        s, e = (set(), set())
        for i in r:
            s.add(i)
            e.add(i)
        while r:
            r.pop()
        while r:
            if r[-1] not in s or r[0] not in e:
                return False
            s.add(r[-1])
            e.add(r[0])
            r.pop()
            r.pop(0)
        return True
    if not t:
        return []
    x = t[91]
    l = [n for n in range(1, x + 1) if is_truncatable(n) and is_prime(n)]
    return l