def all_right_truncatable_prime(x):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True

    def is_truncatable(p):
        if len(str(p)) < 2:
            return True
        return str(p)[-1] in [2, 3, 5, 7] and is_truncatable(int(str(p)[:-1]))
    liste = []
    for i in range(x - 1, 1, -1):
        if is_prime(i) and is_truncatable(i):
            liste.append(i)
    return sorted(liste, reverse=True)